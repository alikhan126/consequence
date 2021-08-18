<template>
  <div
    class="auth-layout-wrap"
    :style="{ backgroundImage: 'url(' + bgImage + ')' }"
  >
    <div class="auth-content">
      <div class="card o-hidden">
        <div class="row">
          <div class="col-md-12">
            <div class="p-4">
              <div class="auth-logo text-center mb-30">
                <img :src="logo" alt="" />
              </div>
              <h1 class="mb-3 text-18">Reset Password</h1>
              <b-form @submit.prevent="submit">
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
                <button
                  class="btn btn-primary btn-block btn-rounded mt-3"
                  variant="primary"
                  :disabled="loading"
                >
                  Change Password
                </button>
              </b-form>

              <div class="mt-3 text-center">
                <router-link to="/signIn" tag="a" class="text-muted">
                  <u>Back to Sign Up</u>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { required, sameAs, minLength } from "vuelidate/lib/validators";
import { mapActions, mapGetters } from "vuex";

export default {
  name: "ResetPassword",
  metaInfo: {
    title: "Reset Password",
  },
  data() {
    return {
      password: "",
      repeatPassword: "",
      submitStatus: null,

      bgImage: require("@/assets/images/photo-wide-4.jpg"),
      logo: require("@/assets/images/new-logo.png"),
      formImage: require("@/assets/images/photo-long-3.jpg"),
    };
  },
  validations: {
    password: {
      required,
      minLength: minLength(8),
    },
    repeatPassword: {
      sameAsPassword: sameAs("password"),
    },
  },
  computed: {
    ...mapGetters(["registeredUser", "loading", "error"]),
  },
  methods: {
    ...mapActions(["reset"]),
    submit() {
      if (this.$v.$invalid) return (this.submitStatus = "ERROR");

      this.reset({
        password1: this.password,
        password2: this.repeatPassword,
        uid: this.$route.params.uid,
        token: this.$route.params.token,
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
        this.makeToast(val.message, "Success");
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
