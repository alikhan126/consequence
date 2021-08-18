<template>
  <div class="main-header">
    <div class="logo text-center font-weight-bold">
      <!-- <img src="@/assets/images/logo.png" alt /> -->
      <span>thdc-virtual-booking</span>
    </div>

    <div @click="sideBarToggle" class="menu-toggle">
      <div></div>
      <div></div>
      <div></div>
    </div>

    <div class="d-flex align-items-center">
      <div class="search-bar md-3">
        <input
          type="text"
          placeholder="Search a Patient"
          @input="searchPatient"
          v-model="searchPatientText"
          v-on-clickaway="resetSearchText"
        />
        <i class="search-icon text-muted i-Magnifi-Glass1"></i>
        <div class="search-patient-dropdown" v-if="searchPatientText">
          <ul>
            <li v-for="(patient, index) in searchPatients" :key="index">
              <div class="search-patient-info">
                <div class="search-patient-name">
                  <h5>{{ patient.first_name }} {{ patient.last_name }}</h5>
                </div>
                <div class="search-patient-detail">
                  <span>9876543210</span>
                  <span>12/3/2021</span>
                </div>
              </div>
            </li>
            <li class="p-3 text-center" v-if="!searchPatients.length">
              No record found
            </li>
          </ul>
        </div>
      </div>

      <!-- Header Icons -->
    </div>
    <div class="d-flex">
      <i
        class="
          i-Add-User
          cursor-pointer
          header-icon
          d-none d-sm-inline-block
          font-weight-bold
        "
        v-b-popover.hover.bottom="'Add Patient'"
        @click="openNewPatientModal"
      >
      </i>
      <!-- <i
            class="i-Magnifi-Glass- cursor-pointer header-icon d-none d-sm-inline-block font-weight-bold"
            v-b-popover.hover.bottom="'Advanced Patient Search'"
          >
          </i> -->
    </div>

    <div style="margin: auto"></div>

    <div class="header-part-right">
      <div class="dropdown location">
        <b-dropdown
          id="dropdown"
          text="Dropdown Button"
          toggle-class="text-decoration-none"
          no-caret
          variant="button"
        >
          <template slot="button-content">
            <i
              class="i-Home1 header-icon"
              role="button"
              id="dropdownMenuButton"
              data-toggle="dropdown"
              aria-haspopup="true"
              aria-expanded="false"
            ></i>
            <span
              class="text-decoration-none text-14 cursor-pointer"
              style="text-decoration: none"
            >
              {{ cloudBase.clinic ? cloudBase.clinic : "Cloud Based..." }}
              <i
                class="
                  i-Arrow-Down
                  text-20
                  cursor-pointer
                  header-icon
                  d-sm-inline-block
                "
                v-b-popover.hover.bottom="'Client - Location'"
              >
              </i>
            </span>
          </template>
          <div class="menu-icon-grid p-3 border-dark">
            <div class="form-group w-100">
              <b-form>
                <div class="form-group">
                  <b-form-select
                    id="input-3"
                    v-model="cloudBase.clinic"
                    :options="cloudBase.clinics"
                    required
                  >
                  </b-form-select>
                </div>
              </b-form>
            </div>
          </div>
        </b-dropdown>
      </div>
      <div
        :class="{ show: isMegaMenuOpen }"
        class="dropdown mega-menu d-none d-md-block"
        v-on-clickaway="closeMegaMenu"
      >
        <a
          href="#"
          class="btn text-muted dropdown-toggle mr-3"
          id="dropdownMegaMenuButton"
          data-toggle="dropdown"
          aria-haspopup="true"
          aria-expanded="false"
          @click="toggleMegaMenu"
          ><i class="fa fa-cog"></i
        ></a>
        <div
          class="dropdown-menu text-left"
          :class="{ show: isMegaMenuOpen }"
          aria-labelledby="dropdownMegaMenuButton"
        >
          <div class="p-4 text-left">
            <div class="menu-icon-grid w-auto p-0">
              <a
                href="#"
                @click="$router.push(option.route)"
                v-for="option in megaMenuOptions"
                :key="option.id"
              >
                <i :class="option.icon"></i> {{ option.title }}
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
    <PatientInfoPanel />
  </div>

  <!-- header top menu end -->
</template>
<script>
import Util from "@/utils";
import PatientInfoPanel from "../../../components/patient-info-panel/patient-info-panel.vue";
import { isMobile } from "mobile-device-detect";
import { mapGetters, mapActions } from "vuex";
import * as moment from "moment";
import { mixin as clickaway } from "vue-clickaway";

export default {
  name: "TopNavBar",
  mixins: [clickaway],
  components: {
    PatientInfoPanel,
  },

  data() {
    return {
      headerSearch: "",
      isDisplay: true,
      isStyle: true,
      isSearchOpen: false,
      isMouseOnMegaMenu: true,
      isMegaMenuOpen: false,
      searchPatientText: "",
      patientsList: [],
      megaMenuOptions: [
        {
          id: 1,
          title: "Schedule",
          icon: "i-Shop-4",
          route: "/app/schedule",
        },
        {
          id: 2,
          title: "Users",
          icon: "i-Administrator",
          route: "/app/users",
        },
        {
          id: 3,
          title: "Insights",
          icon: "i-Bar-Chart",
          route: "/app/insights",
        },
      ],
      patientData: {
        name: "",
        dob: "",
        selectedTime: moment().format("HH:MM:ss"),
        selectedDate: new Date(),
      },
      cloudBase: {
        clinic: "Cloud Based...",
        clinics: ["Cloud Based...", "Clinic1", "Clinic2", "Clinic3"],
        location: null,
        locations: [
          { text: "Select Location", value: null },
          "USD",
          "Canada",
          "Africa",
          "Australia",
        ],
      },
    };
  },
  mounted() {
    this.patientsList = this.getPatientsList;
  },
  computed: {
    ...mapGetters(["getSideBarToggleProperties", "getPatientsList"]),
  },

  methods: {
    ...mapActions([
      "changeSecondarySidebarProperties",
      "changeSidebarProperties",
      "changeThemeMode",
      "logout",
      "setPatientData",
      "setActiveTabInPatientForm",
    ]),
    // megaMenuToggle() {
    //   this.isMegaMenuOpen = false;

    //   console.log("work");
    // },

    handleFullScreen() {
      Util.toggleFullScreen();
    },
    logoutUser() {
      this.logout();

      this.$router.push("/app/sessions/signIn");
    },

    closeMegaMenu() {
      this.isMegaMenuOpen = false;
      // console.log(this.isMouseOnMegaMenu);
      // if (!this.isMouseOnMegaMenu) {
      //   this.isMegaMenuOpen = !this.isMegaMenuOpen;
      // }
    },
    toggleMegaMenu() {
      this.isMegaMenuOpen = !this.isMegaMenuOpen;
    },
    toggleSearch() {
      this.isSearchOpen = !this.isSearchOpen;
    },
    searchPatient(e) {
      const searchInput = e.target.value;
      let searchResult = [];
      if (searchInput) {
        const value =
          searchInput.charAt(0).toUpperCase() + searchInput.slice(1);
        searchResult = this.patientsList.filter((patient) => {
          return (
            patient.first_name.indexOf(value) > -1 ||
            patient.last_name.indexOf(value) > -1
          );
        });
      } else {
        searchResult = [];
      }
      this.searchPatients = searchResult;
    },
    resetSearchText() {
      this.searchPatientText = "";
    },
    openAppointmentModal() {},
    openNewPatientModal() {
      this.setPatientData({
        first_name: "",
        last_name: "",
        gender: "",
        dob: null,
        id: null,
      });
      this.setActiveTabInPatientForm("contact");
      this.$root.$emit("bv::toggle::collapse", "sidebar-right");
    },
    sideBarToggle(el) {
      if (
        this.getSideBarToggleProperties.isSideNavOpen &&
        this.getSideBarToggleProperties.isSecondarySideNavOpen &&
        isMobile
      ) {
        this.changeSidebarProperties();
        this.changeSecondarySidebarProperties();
      } else if (
        this.getSideBarToggleProperties.isSideNavOpen &&
        this.getSideBarToggleProperties.isSecondarySideNavOpen
      ) {
        this.changeSecondarySidebarProperties();
      } else if (this.getSideBarToggleProperties.isSideNavOpen) {
        this.changeSidebarProperties();
      } else if (
        !this.getSideBarToggleProperties.isSideNavOpen &&
        !this.getSideBarToggleProperties.isSecondarySideNavOpen &&
        !this.getSideBarToggleProperties.isActiveSecondarySideNav
      ) {
        this.changeSidebarProperties();
      } else if (
        !this.getSideBarToggleProperties.isSideNavOpen &&
        !this.getSideBarToggleProperties.isSecondarySideNavOpen
      ) {
        // console.log("4");

        this.changeSidebarProperties();
        this.changeSecondarySidebarProperties();
        // console.log("4");
      }
    },
  },
};
</script>



