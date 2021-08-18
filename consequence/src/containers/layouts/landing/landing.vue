<template>
  <div>
    <Header />
    <div class="landing-wrap">
      <div class="w-100 h-100">
        <b-row class="align-items-center">
          <b-col lg="6">
            <div class="banner-image">
              <img src="@/assets/images/banner-image.svg" alt />
            </div>
          </b-col>
          <b-col lg="6">
            <div class="banner-content">
              <h2>Manage Your Dental Practice Better.</h2>
              <p>
                Vertically integrated PMS, EHR & Telehealth platform for fast
                patient scheduling & management.
              </p>
              <a href="" class="btn btn-white"> Get Stearted</a>
            </div>
          </b-col>
        </b-row>
      </div>
    </div>
    <Footer />
  </div>
</template>

<style lang="scss">
.landing-wrap {
  min-height: -moz-calc(100vh - 53px);
  min-height: -webkit-calc(100vh - 53px);
  min-height: calc(100vh - 53px);
  padding: 230px 60px 110px;
  background-color: #6cdcd4;
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
  overflow: hidden;
}
.banner-image {
  position: relative;
  padding: 40px;
  max-width: 680px;
  margin: 0 auto;
  z-index: 1;
}
.banner-image:before {
  position: absolute;
  content: "";
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  background-color: rgba(255, 255, 255, 0.6);
  border-radius: 100%;
  -moz-transform: rotate(-55deg);
  -webkit-transform: rotate(-55deg);
  transform: rotate(-55deg);
  margin: -70px;
  z-index: -1;
}
.banner-content h2 {
  color: #fff;
  font-size: 80px;
  font-weight: bold;
}
.banner-content p {
  color: #fff;
  font-size: 30px;
}
.btn.btn-white {
  color: #6cdcd4;
  background-color: #fff;
  padding: 10px 40px;
  border-radius: 40px;
  font-size: 18px;
  font-weight: bold;
  box-shadow: 0 3px 0 rgba(0, 0, 0, 0.1);
}
@media screen and (max-width: 1700px) {
  .banner-content h2 {
    font-size: 50px;
  }
  .banner-image:before {
    margin: -50px;
  }
}
@media screen and (max-width: 1199px) {
  .banner-content h2 {
    font-size: 36px;
  }
  .logo {
    max-width: 250px;
  }
}
@media screen and (max-width: 991px) {
  .banner-image {
    margin: 0 auto 140px;
  }
  .landing-wrap {
    padding: 220px 60px 100px;
  }
  .banner-image {
    max-width: 550px;
  }
}
@media screen and (max-height: 767px) {
  .banner-image {
    max-width: 400px;
  }
  .landing-wrap {
    padding: 130px 60px 50px;
  }
}
</style>
<script>
import Header from "../global-header/global-header.vue";
import Footer from "../global-footer/global-footer.vue";

export default {
  components: { Header, Footer },
  data() {
    return {};
  },
  computed: {},
  methods: {},
};
</script>