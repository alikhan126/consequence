<template>
  <div
    class="auth-layout-wrap"
    :style="{ backgroundImage: 'url(' + bgImage + ')' }"
  >
    <div class="auth-content">
      <div class="card o-hidden">
        <div class="row">
          <div class="col-md-12">
            <div class="p-5">
              <div class="auth-logo text-center mb-30">
                <img :src="logo" alt="" />
              </div>
              <h1 class="mb-3 text-18">Forgot Password</h1>
              <b-form @submit.prevent="submit">
                <b-form-group label="Your Email">
                  <b-form-input
                    id="email"
                    v-model="email"
                    v-model.trim="$v.email.$model"
                    class="form-control form-control-rounded"
                    type="email"
                  >
                  </b-form-input>

                  <b-alert
                    show
                    variant="danger"
                    class="error col mt-1"
                    v-if="$v.email.$error"
                    >Email must be required.</b-alert
                  >
                </b-form-group>
                <button
                  class="btn btn-primary btn-block btn-rounded mt-3"
                  variant="primary"
                  :disabled="loading"
                >
                  Submit
                  <span v-if="loading">...</span>
                </button>
              </b-form>
              <div class="mt-3 text-center">
                <router-link to="signIn" tag="a" class="text-muted">
                  <u>Back to Sign In</u>
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
import { required } from "vuelidate/lib/validators";
import { mapActions, mapGetters } from "vuex";

export default {
  name: "forgot",
  metaInfo: {
    // if no subcomponents specify a metaInfo.title, this title will be used
    title: "Forgot Password",
  },
  data() {
    return {
      email: "",
      submitStatus: null,

      bgImage: require("@/assets/images/photo-wide-4.jpg"),
      logo: require("@/assets/images/new-logo.png"),
      formImage: require("@/assets/images/photo-long-3.jpg"),
    };
  },
  validations: {
    email: {
      required,
    },
  },
  computed: {
    ...mapGetters(["registeredUser", "loading", "error"]),
  },
  methods: {
    ...mapActions(["forgot"]),
    submit() {
      if (this.$v.$invalid) return (this.submitStatus = "ERROR");

      this.forgot({ email: this.email });
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
          this.$router.push("/signin");
        }, 1000);
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
