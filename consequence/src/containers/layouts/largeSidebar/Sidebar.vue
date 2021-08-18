<template>
  <div
    class="side-content-wrap"
    @mouseenter="isMenuOver = true"
    @mouseleave="isMenuOver = false"
    @touchstart="isMenuOver = true"
  >
    <vue-perfect-scrollbar
      :settings="{ suppressScrollX: true, wheelPropagation: false }"
      :class="{ open: getSideBarToggleProperties.isSideNavOpen }"
      ref="myData"
      class="sidebar-left rtl-ps-none ps scroll"
    >
      <div class="main-menu">
        <div class="nav-menu">
          <ul class="navigation-left">
            <li
              @mouseenter="toggleSubMenu"
              :class="{ active: selectedParentMenu == 'appointments' }"
              class="nav-item"
              data-item="appointments"
              :data-submenu="true"
            >
              <router-link tag="a" class="nav-item-hold" to="/app/appointments">
                <i class="nav-icon i-File-Horizontal-Text"></i>
                <span class="nav-text">Appointments</span>
              </router-link>
              <div class="triangle"></div>
            </li>
          </ul>
        </div>
        <div class="sidenav-bottom">
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
                <span>{{ "Guest" }}</span>
                <i class="i-Arrow-Down"></i>
              </template>

              <div class="dropdown-menu-right" aria-labelledby="userDropdown">
                <div class="dropdown-header">
                  <i class="i-Lock-User mr-1"></i>
                  {{ "Guest" }}
                </div>
                <a class="dropdown-item">Change Password</a>
                <a class="dropdown-item" href="#" @click.prevent="logoutUser"
                  >Sign out</a
                >
              </div>
            </b-dropdown>
          </div>
        </div>
      </div>
    </vue-perfect-scrollbar>
  </div>
  <!--=============== Left side End ================-->
</template>

<script>
import Topnav from "./TopNav";
import { isMobile } from "mobile-device-detect";

import { mapGetters, mapActions } from "vuex";

export default {
  components: {
    Topnav,
  },

  data() {
    return {
      isDisplay: true,
      isMenuOver: false,
      isStyle: true,
      selectedParentMenu: "",
      isMobile,
    };
  },
  mounted() {
    this.toggleSelectedParentMenu();
    window.addEventListener("resize", this.handleWindowResize);
    document.addEventListener("click", this.returnSelectedParentMenu);
    this.handleWindowResize();
  },

  beforeDestroy() {
    document.removeEventListener("click", this.returnSelectedParentMenu);
    window.removeEventListener("resize", this.handleWindowResize);
  },
  computed: {
    ...mapGetters(["getSideBarToggleProperties"]),
  },

  methods: {
    ...mapActions([
      "changeSecondarySidebarProperties",
      "changeSecondarySidebarPropertiesViaMenuItem",
      "changeSecondarySidebarPropertiesViaOverlay",
      "changeSidebarProperties",
      "logout"
    ]),

    handleWindowResize() {
      //  console.log('not working is Mobile');
      if (window.innerWidth <= 1200) {
        if (this.getSideBarToggleProperties.isSideNavOpen) {
          this.changeSidebarProperties();
        }
        if (this.getSideBarToggleProperties.isSecondarySideNavOpen) {
          this.changeSecondarySidebarProperties();
        }
      } else {
        if (!this.getSideBarToggleProperties.isSideNavOpen) {
          this.changeSidebarProperties();
        }
      }
    },
    toggleSelectedParentMenu() {
      const currentParentUrl = this.$route.path
        .split("/")
        .filter((x) => x !== "")[1];

      if (currentParentUrl !== undefined || currentParentUrl !== null) {
        this.selectedParentMenu = currentParentUrl.toLowerCase();
      } else {
        this.selectedParentMenu = "dashboards";
      }
    },
    toggleSubMenu(e) {
      let hasSubmenu = e.target.dataset.submenu;
      let parent = e.target.dataset.item;
      this.selectedParentMenu = parent;
      // if (hasSubmenu) {
      //   this.changeSecondarySidebarPropertiesViaMenuItem(true);
      // } else {
      //   this.selectedParentMenu = parent;
      //   this.changeSecondarySidebarPropertiesViaMenuItem(false);
      // }
    },

    removeOverlay() {
      this.changeSecondarySidebarPropertiesViaOverlay();
      if (window.innerWidth <= 1200) {
        this.changeSidebarProperties();
      }
      this.toggleSelectedParentMenu();
    },
    returnSelectedParentMenu() {
      if (!this.isMenuOver) {
        this.toggleSelectedParentMenu();
      }
    },
    logoutUser() {
      this.logout();
      setTimeout(() => {
        this.$router.push("/signIn");
      }, 500);
    },
    toggleSidebarDropdwon(event) {
      let dropdownMenus = this.$el.querySelectorAll(".dropdown-sidemenu.open");

      event.currentTarget.classList.toggle("open");

      dropdownMenus.forEach((dropdown) => {
        dropdown.classList.remove("open");
      });
    },
  },
};
</script>

<style lang="" scoped>
</style>
