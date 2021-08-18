<template>
  <vue-perfect-scrollbar
    class="sidebar-panel rtl-ps-none ps scroll"
    @mouseleave.native="
      sidebarCompact();
      returnSelectedParentMenu();
    "
    @mouseenter.native="removeSidebarCompact"
    :class="{
      'vertical-sidebar-compact': getVerticalCompact.isSidebarCompact,
      'sidebar-full-collapse': getVerticalSidebar.isMobileCompact,
    }"
    :settings="{ suppressScrollX: true, wheelPropagation: false }"
  >
    <div
      class="
        gull-brand
        text-center
        d-flex
        align-items-center
        pl-2
        mb-4
        justify-content-center
      "
    >
      <img class="logo" src="@/assets/images/new-logo.png" />
    </div>

    <div class="close-mobile-menu" @click="mobileSidebar">
      <i class="text-16 text-primary i-Close-Window font-weight-bold"></i>
    </div>

    <div class="mt-5 main-menu">
      <div class="nav-menu">
        <ul class="ul-vertical-sidebar pl-4" id="menu">
          <li class="hover-menu" v-for="menu in sideMenu" :key="menu.title">
            <div>
              <router-link
                tag="a"
                class="has-arrow"
                :to="menu.redirectTo"
                :class="{
                  active: selectedParentMenu === menu.selectedParentMenu,
                }"
              >
                <i
                  :class="`${menu.icon} text-23 mr-2 icon font-weight-bold`"
                  v-b-popover.hover.right="menu.title"
                ></i>
                <span
                  class="text-14"
                  :class="{
                    'vertical-item-name': getVerticalCompact.isItemName,
                  }"
                  >{{ menu.title }}</span
                >
              </router-link>
            </div>
          </li>
        </ul>
      </div>

      <div class="sidenav-bottom">
        <!-- <ul class="ul-vertical-sidebar pl-4 mb-0" id="menu">
          <li class="hover-menu hover-dropdown">
            <div v-b-toggle.collapse-3>
              <a
                class="has-arrow"
                href="#"
                :class="{ active: selectedParentMenu == 'settings' }"
              >
                <i class="i-Globe text-23 mr-2 icon font-weight-bold"></i>
                <span
                  class="text-15"
                  :class="{
                    'vertical-item-name': getVerticalCompact.isItemName,
                  }"
                  >Settings</span
                >
              </a>
            </div>
            <b-collapse id="collapse-3">
              <ul
                class="Ul_collapse"
                :class="{ 'vertical-item-name': getVerticalCompact.isItemName }"
              >
                <li class="item-name">
                  <router-link tag="a" to="/app/schedule-template">
                    <span class>Schedule Template</span>
                  </router-link>
                </li>
                <li class="item-name">
                  <router-link tag="a" to="/app/virtual-consults">
                    <span class>Virtual-Consults</span>
                  </router-link>
                </li>
                <li class="item-name">
                  <router-link tag="a" to="/app/users">
                    <span class>Users</span>
                  </router-link>
                </li>
                <li class="item-name">
                  <router-link tag="a" to="/app/locations">
                    <span class>Locations</span>
                  </router-link>
                </li>
                <li class="item-name">
                  <router-link tag="a" to="/app/location-hours">
                    <span class>Location Hours</span>
                  </router-link>
                </li>
                <li class="item-name">
                  <router-link tag="a" to="/app/operatories">
                    <span class>Operatories</span>
                  </router-link>
                </li>
              </ul>
            </b-collapse>
          </li>
        </ul> -->

        <div class="dropdown">
          <b-dropdown
            id="dropdown-1"
            right
            text="Right align"
            class="m-md-2 user col align-self-end"
            toggle-class="text-decoration-none"
            no-caret
            variant="button"
          >
            <template slot="button-content">
              <img
                src="@/assets/images/faces/1.jpg"
                id="userDropdown"
                alt
                data-toggle="dropdown"
                aria-haspopup="true"
                aria-expanded="false"
              />
              <span>{{
                (loggedInUser && loggedInUser.username) || "Guest"
              }}</span>
              <i class="i-Arrow-Down"></i>
            </template>

            <div class="dropdown-menu-right" aria-labelledby="userDropdown">
              <div class="dropdown-header">
                <i class="i-Lock-User mr-1"></i>
                {{ (loggedInUser && loggedInUser.username) || "Guest" }}
              </div>
              <!-- <a class="dropdown-item">Change Password</a> -->
              <a class="dropdown-item" href="#" @click.prevent="logoutUser"
                >Sign out</a
              >
            </div>
          </b-dropdown>
        </div>
      </div>
    </div>
  </vue-perfect-scrollbar>
</template>
<script>
import { mapGetters, mapActions } from "vuex";
export default {
  components: {},
  computed: {
    ...mapGetters(["getVerticalCompact", "getVerticalSidebar", "loggedInUser"]),
  },
  data() {
    return {
      selectedParentMenu: "",
      sideMenu: [
        {
          title: "Bank Accounts",
          selectedParentMenu: "appointments",
          icon: "i-File-Horizontal-Text",
          redirectTo: "/app/appointments",
        },
        {
          title: "Cards",
          selectedParentMenu: "appointments",
          icon: "i-File-Horizontal-Text",
          redirectTo: "/app/appointments",
        },
      ],
    };
  },
  mounted() {
    this.toggleSelectedParentMenu();
    document.addEventListener("click", this.returnSelectedParentMenu);
  },
  beforeDestroy() {
    document.removeEventListener("click", this.returnSelectedParentMenu);
  },
  methods: {
    ...mapActions([
      "logout",
      "switchSidebar",
      "sidebarCompact",
      "removeSidebarCompact",
      "mobileSidebar",
    ]),

    toggleSelectedParentMenu() {
      const currentParentUrl = this.$route.path
        .split("/")
        .filter((x) => x !== "")[1];
      if (currentParentUrl !== undefined || currentParentUrl !== null) {
        this.selectedParentMenu = currentParentUrl.toLowerCase();
      } else {
        this.selectedParentMenu = "daily-huddle";
      }
    },
    returnSelectedParentMenu() {
      this.toggleSelectedParentMenu();
    },
    logoutUser() {
      this.logout();
    },
  },
  watch: {
    loggedInUser(val) {
      if (val === null) {
        setTimeout(() => {
          this.$router.push("/signIn");
        }, 500);
      }
    },
  },
};
</script>
<style>
.logo {
  max-width: 100px;
}
</style>