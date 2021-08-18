import Vue from "vue";
import store from "./store";
// import {isMobile} from "mobile-device-detect";
import Router from "vue-router";
import authenticate from "./auth/authenticate";
import unAuthenticate from "./auth/unAuthenticate";

Vue.use(Router);

import AppView from "./views/app/index.vue";
import Schedule from "./views/app/schedule/schedule.vue";
import Users from "./views/app/users/users.vue";
import Appointments from "./views/app/appointments/appointments.vue";
import Insights from "./views/app/insights/insights.vue";
import signIn from "./views/app/sessions/signIn";
import signUp from "./views/app/sessions/signUp.vue";
import forgot from "./views/app/sessions/forgot.vue";
import reset from "./views/app/sessions/reset.vue";
import VideoCall from "./views/app/video-call/video-call.vue";

// Extra components
import home from "./auth/home";

// create new router
const routes = [
  {
    path: "/",
    beforeEnter: home,
  },
  // Sessions
  {
    path: "/signIn",
    name: "Login",
    beforeEnter: unAuthenticate,
    component: signIn,
  },
  {
    path: "/signUp",
    name: "Register",
    beforeEnter: unAuthenticate,
    component: signUp,
  },
  {
    path: "/forgot",
    name: "Forgot",
    beforeEnter: unAuthenticate,
    component: forgot,
  },
  {
    path: "/reset-password/:uid/:token",
    name: "Reset",
    beforeEnter: unAuthenticate,
    component: reset,
  },
  // App
  {
    path: "/app",
    name: "HomePageDashboard",
    component: AppView,
    beforeEnter: authenticate,
    redirect: "./app/appointments",
    children: [
      {
        path: "/app/appointments",
        component: Appointments,
      },
      {
        path: "/app/schedule",
        component: Schedule,
      },
      {
        path: "/app/users",
        component: Users,
      },
      {
        path: "/app/insights",
        component: Insights,
      },
      {
        path: "/app/overview",
        component: () => import("./views/app/chart/echart"),
      },
      {
        path: "/app/settings",
        component: () => import("./views/app/pages/profile"),
      },
      {
        path: "/app/video-call",
        component: VideoCall,
      },
    ],
  },
  {
    path: "*",
    component: () => import("./views/app/pages/notFound"),
  },
];

const router = new Router({
  mode: "history",
  linkActiveClass: "open",
  routes,
  scrollBehavior(to, from, savedPosition) {
    return { x: 0, y: 0 };
  },
});

router.afterEach(() => {
  // Remove initial loading
  // Complete the animation of the route progress bar.
  // if (isMobile) {
  const preLoading = document.getElementById("page-loader");
  if (preLoading) {
    preLoading.classList.add("hide");
  }
  if (window.innerWidth <= 1200) {
    // console.log("mobile");
    store.dispatch("changeSidebarProperties");
    if (store.getters.getSideBarToggleProperties.isSecondarySideNavOpen) {
      store.dispatch("changeSecondarySidebarProperties");
    }

    if (store.getters.getCompactSideBarToggleProperties.isSideNavOpen) {
      store.dispatch("changeCompactSidebarProperties");
    }
  } else {
    if (store.getters.getSideBarToggleProperties.isSecondarySideNavOpen) {
      store.dispatch("changeSecondarySidebarProperties");
    }

    // store.state.sidebarToggleProperties.isSecondarySideNavOpen = false;
  }
});

export default router;
