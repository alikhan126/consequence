<template>
  <div class="header-wrap">
    <div class="logo">
      <img src="@/assets/images/new-logo.png" alt />
    </div>

    <div class="globle-header nav-bar">
      <nav>
        <ul class="nav-menu">
          <!-- <li><a href="javascript:void(0)" @click="$router.push('/contact')">Contact</a></li> -->
          <li><a href="javascript:void(0)" @click="$router.push('/book-appointment')">Book Appointment</a></li>
          <li><a href="javascript:void(0)" @click="$router.push('/signIn')">Login</a></li>
        </ul>
        <ul class="nav-social">
          <li>
            <a href=""><i class="fa fa-instagram"></i></a>
          </li>
          <li>
            <a href=""><i class="fa fa-facebook"></i></a>
          </li>
          <li>
            <a href=""><i class="fa fa-twitter"></i></a>
          </li>
        </ul>
      </nav>
    </div>
  </div>
</template>

<style lang="scss">
.header-wrap {
  padding: 15px 60px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: transparent;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
}
.header-wrap .logo {
  max-width: 200px;
}
.globle-header .nav-menu,
.globle-header .nav-social {
  margin: 0;
  padding: 0;
}
.globle-header .nav-menu li,
.globle-header .nav-social li {
  list-style: none;
  float: left;
}
.globle-header .nav-menu li a {
  font-size: 20px;
  padding: 0 10px;
  color: #fff;
}
.globle-header .nav-menu li a:hover,
.globle-header .nav-social li a:hover {
  color: #000;
}
.globle-header .nav-social li a {
  font-size: 25px;
  padding: 0 10px;
  color: #fff;
}
.globle-header.nav-bar nav {
  display: flex;
  align-items: center;
}
</style>

<script>
export default {
  components: {},
  data() {
    return {};
  },
  computed: {},
  methods: {},
};
</script>