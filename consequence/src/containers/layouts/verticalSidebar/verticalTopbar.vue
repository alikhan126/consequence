<template>
  <div class="mb-30">
    <header class="main-header vertical-header d-flex">
      <div class="menu-toggle vertical-toggle" @click="mobileSidebar">
        <div></div>
        <div></div>
        <div></div>
      </div>

      <!-- <div
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
          aria-labelledby="dropdownMenuButton"
        >
          <div class="row m-0">
            <div class="p-4 text-left">
              <div class="menu-icon-grid w-auto p-0">
                
              </div>
            </div>
          </div>
        </div>
      </div> -->

      <div class="header-toggle">
        <div class="search-bar">
          <i class="search-icon text-muted i-Magnifi-Glass1"></i>
          <input
            type="text"
            placeholder="Search a Patient"
            @input="searchPatient"
            v-model="searchPatientText"
            v-on-clickaway="resetSearchText"
          />
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
      </div>

      <div class="header-part-right">
        <!-- <b-form-datepicker
          :date-format-options="{
            year: 'numeric',
            month: '2-digit',
            day: '2-digit',
          }"
          id="example-datepicker"
          v-model="selectedDate"
          class="datepicker-input"
        ></b-form-datepicker> -->

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
    </header>
  </div>
</template>
<script>
import { mapGetters, mapActions } from "vuex";
import * as moment from "moment";
import { mixin as clickaway } from "vue-clickaway";
import Util from "@/utils";
import PatientInfoPanel from "../../../components/patient-info-panel/patient-info-panel.vue";

export default {
  mixins: [clickaway],
  components: { PatientInfoPanel },
  computed: {
    ...mapGetters([
      "getVerticalCompact",
      "getVerticalSidebar",
      "getSideBarToggleProperties",
      "getPatientsList",
    ]),
  },
  data() {
    return {
      isMegaMenuOpen: false,
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
      selectedDate: new Date(),
      searchPatientText: "",
      appointmentData: {
        searchPatientText: "",
        selectedTime: moment().format("HH:MM:ss"),
        selectedDate: new Date(2018, 7, 1),
      },
      patientData: {
        name: "",
        dob: "",
        selectedTime: moment().format("HH:MM:ss"),
        selectedDate: new Date(),
      },
      options2: [
        { value: "1", text: "aa" + " - " + "1" },
        { value: "2", text: "ab" + " - " + "2" },
        { value: "3", text: "bc" + " - " + "3" },
        { value: "4", text: "cd" + " - " + "4" },
        { value: "5", text: "de" + " - " + "5" },
      ],

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
  methods: {
    ...mapActions([
      "logout",
      "switchSidebar",
      "sidebarCompact",
      "removeSidebarCompact",
      "mobileSidebar",
      "setPatientData",
      "setActiveTabInPatientForm",
    ]),
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
    handleFullScreen() {
      Util.toggleFullScreen();
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
  },
  mounted() {
    this.patientsList = this.getPatientsList;
  },
  watch: {
    // dateSelected(val){
    // }
  },
};
</script>>