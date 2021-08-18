<template>
  <div>
    <Header />
    <div class="contact-wrap">
      <div class="conteiner">
        <b-row class="justify-content-center">
          <b-col md="6" lg="6">
            <h3 class="contact-title">Talk to the Dr. H & Co team.</h3>
            <div class="contact-form">
              <b-form-group>
                <b-form-input
                  type="text"
                  required
                  placeholder="What's your business name?"
                ></b-form-input>
              </b-form-group>
              <b-form-group>
                <b-form-input
                  type="email"
                  required
                  placeholder="What's your business email?"
                ></b-form-input>
              </b-form-group>
              <b-form-group>
                <b-button block class="btn-outline-white">Send</b-button>
              </b-form-group>
            </div>
          </b-col>
        </b-row>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script>
import Header from "../global-header/global-header";
import Footer from "../global-footer/global-footer";
export default {
  components: { Header, Footer },
  data() {
    return {};
  },
  computed: {},
  methods: {},
};
</script>
<style lang="scss">
.contact-wrap {
  min-height: 100vh;
  padding: 150px 60px;
  background-color: #6cdcd4;
}
.contact-title {
  text-align: center;
  color: #fff;
  font-size: 40px;
  font-weight: 600;
}
.contact-form input {
  background-color: transparent;
  color: #fff;
  height: auto;
  padding: 20px 0;
  font-size: 20px;
  border-left: 0;
  border-right: 0;
  border-top: 0;
  border-radius: 0;
  border-bottom: 3px solid #fff;
}

.contact-form input:focus {
  background-color: transparent;
  color: #fff;
}

.contact-form .form-group {
  margin-top: 60px;
}

.btn.btn-outline-white {
  padding: 15px 0;
  border-radius: 10px;
  border-color: #fff;
  background-color: transparent !important;
  font-size: 20px;
  color: #fff !important;
  border-width: 1px;
}
.btn.btn-outline-white:hover,
.btn.btn-outline-white:focus,
.btn.btn-outline-white:active {
  border-color: #fff !important;
  color: #fff !important;
  box-shadow: none !important;
  outline: none !important;
}

.contact-form input::-webkit-input-placeholder {
  /* Chrome/Opera/Safari */
  color: #fff;
}
.contact-form input::-moz-placeholder {
  /* Firefox 19+ */
  color: #fff;
}
.contact-form input:-ms-input-placeholder {
  /* IE 10+ */
  color: #fff;
}
.contact-form input:-moz-placeholder {
  /* Firefox 18- */
  color: #fff;
}
</style>