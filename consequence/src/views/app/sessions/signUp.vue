<template>
  <!--  -->
  <div
    :style="{ backgroundImage: 'url(' + bgImage + ')' }"
    class="auth-layout-wrap"
  >
    <div class="auth-content">
      <div class="card o-hidden">
        <div class="row">
          <div
            class="col-md-6 text-center"
            style="background-size: cover"
            :style="{ backgroundImage: 'url(' + signInImage + ')' }"
          >
            <div class="pl-3 auth-right">
              <div class="auth-logo text-center mt-4">
                <!-- <img :src="logo" alt="" /> -->
              </div>
              <div class="flex-grow-1"></div>
              <div class="w-100 mb-30">
                <router-link
                  to="signIn"
                  class="
                    btn
                    btn-outline-primary
                    btn-outline-email
                    btn-block
                    btn-icon-text
                    btn-rounded
                  "
                  href="signin.html"
                >
                  <i class="i-Mail-with-At-Sign"></i> Sign in with Email
                </router-link>
              </div>
              <div class="flex-grow-1"></div>
            </div>
          </div>

          <b-col md="6">
            <div class="p-4">
              <h1 class="mb-3 text-18">Sign Up</h1>
              <b-form @submit.prevent="submit">
                <b-form-group label="Username">
                  <b-form-input
                    class="form-control form-control-rounded"
                    label="Name"
                    v-model.trim="$v.username.$model"
                  >
                  </b-form-input>

                  <b-alert
                    show
                    variant="danger"
                    class="error col mt-1"
                    v-if="!$v.username.minLength"
                    >Username must have at least
                    {{ $v.username.$params.minLength.min }} letters.</b-alert
                  >
                </b-form-group>


                <b-form-group label="Email">
                  <b-form-input
                    class="form-control form-control-rounded"
                    label="Name"
                    type="email"
                    v-model="email"
                  >
                  </b-form-input>
                </b-form-group>

                <b-form-group label="Password">
                  <b-form-input
                    class="form-control form-control-rounded"
                    label="Name"
                    type="password"
                    v-model.trim="$v.password.$model"
                  >
                  </b-form-input>

                  <b-alert
                    show
                    variant="danger"
                    class="error col mt-1"
                    v-if="!$v.password.minLength"
                    >Minimum
                    {{ $v.password.$params.minLength.min }} charaters.</b-alert
                  >
                </b-form-group>

                <b-form-group label="Repeat Password">
                  <b-form-input
                    class="form-control form-control-rounded"
                    label="Name"
                    type="password"
                    v-model.trim="$v.repeatPassword.$model"
                  >
                  </b-form-input>

                  <b-alert
                    show
                    variant="danger"
                    class="error col mt-1"
                    v-if="!$v.repeatPassword.sameAsPassword"
                    >Passwords must be identical.</b-alert
                  >
                </b-form-group>

                <b-button
                  type="submit"
                  block
                  variant="primary"
                  class="btn-rounded"
                  :disabled="loading"
                  >Sign Up
                  <span v-if="loading">...</span>
                </b-button>

                <div class="mt-3 text-center">
                  <router-link to="signIn" tag="a" class="text-muted">
                    <u>Back to Sign In</u>
                  </router-link>
                </div>
              </b-form>
            </div>
          </b-col>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { required, sameAs, minLength } from "vuelidate/lib/validators";
import { mapGetters, mapActions } from "vuex";
export default {
  name: "siginUp",
  metaInfo: {
    title: "SignUp",
  },

  data() {
    return {
      username: "",
      email: "",
      password: "",
      repeatPassword: "",
      bgImage: require("@/assets/images/photo-wide-4.jpg"),
      logo: require("@/assets/images/new-logo.png"),
      signInImage: require("@/assets/images/photo-long-3.jpg"),
      submitStatus: null,
    };
  },

  validations: {
    username: {
      required,
      minLength: minLength(4),
    },
    password: {
      required,
      minLength: minLength(5),
    },
    repeatPassword: {
      sameAsPassword: sameAs("password"),
    },
  },

  computed: {
    ...mapGetters(["registeredUser", "loading", "error"]),
  },

  methods: {
    ...mapActions(["register"]),
    submit() {
      this.$v.$touch();
      if (this.$v.$invalid) return (this.submitStatus = "ERROR");

      this.register({
        username: this.username,
        email: this.email,
        password1: this.password,
        password2: this.repeatPassword,
      });
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
    registeredUser(val) {
      if (val != null) {
        this.makeToast(val.message, 'Success');
        setTimeout(() => {
          this.$router.push({ name: "Login" });
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