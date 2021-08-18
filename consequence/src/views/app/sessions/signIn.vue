<template>
  <div
    class="auth-layout-wrap"
    :style="{ backgroundImage: 'url(' + bgImage + ')' }"
  >
    <div class="auth-content">
      <div class="card o-hidden">
        <div class="row">
          <div class="col-md-6">
            <div class="p-4">
              <div class="auth-logo text-center mb-30">
                <!-- <img :src="logo" /> -->
              </div>
              <h1 class="mb-3 text-18">Sign In</h1>
              <b-form @submit.prevent="formSubmit">
                <b-form-group label="Email Address" class="text-12">
                  <b-form-input
                    class="form-control-rounded"
                    type="email"
                    v-model="email"
                    email
                    required
                  ></b-form-input>
                </b-form-group>

                <b-form-group label="Password" class="text-12">
                  <b-form-input
                    class="form-control-rounded"
                    type="password"
                    v-model="password"
                  ></b-form-input>
                </b-form-group>

                <b-button
                  type="submit"
                  tag="button"
                  class="btn-rounded btn-block mt-2 position-relative"
                  variant="primary"
                  :disabled="loading"
                  >Sign In
                  <span v-if="loading">...</span>
                </b-button>

                <b-button
                  to="signUp"
                  block
                  variant="primary mt-2"
                  class="btn-rounded"
                  >Create an account</b-button
                >
              </b-form>

              <div class="mt-3 text-center">
                <router-link to="forgot" tag="a" class="text-muted">
                  <u>Forgot Password?</u>
                </router-link>
              </div>
            </div>
          </div>

          <b-col
            md="6"
            class="text-center"
            style="backgroundsize: cover"
            :style="{ backgroundImage: 'url(' + signInImage + ')' }"
          >
            <div class="pr-3 auth-right">
              <router-link
                to="signUp"
                class="
                  btn
                  btn-rounded
                  btn-outline-primary
                  btn-outline-email
                  btn-block
                  btn-icon-text
                "
                href="signup.html"
              >
                <i class="i-Mail-with-At-Sign"></i> Sign up with Email
              </router-link>
            </div>
          </b-col>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { mapGetters, mapActions } from "vuex";
export default {
  name: "signIn",
  metaInfo: {
    // if no subcomponents specify a metaInfo.title, this title will be used
    title: "SignIn",
  },
  data() {
    return {
      email: "",
      password: "",
      bgImage: require("@/assets/images/photo-wide-4.jpg"),
      logo: require("@/assets/images/new-logo.png"),
      signInImage: require("@/assets/images/photo-long-3.jpg"),
    };
  },
  computed: {
    ...mapGetters(["loggedInUser", "loading", "error"]),
  },
  methods: {
    ...mapActions(["login"]),
    formSubmit() {
      this.login({ email: this.email, password: this.password });
    },
    makeToast(msg, title, variant = "success") {
      this.$bvToast.toast(msg, {
        title: ` ${title || "default"}`,
        variant: variant,
        solid: true,
      });
    },
  },
  watch: {
    loggedInUser(val) {
      if (val && val.access) {
        this.makeToast("Successfully Logged In", "Success");
        setTimeout(() => {
          this.$router.push({ name: "HomePageDashboard" });
        }, 500);
      }
    },
    error(val) {
      if (val != null) {
        this.makeToast(val.message, "Error", "danger");
      }
    },
  },
};
</script>
