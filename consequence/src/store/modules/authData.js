import axios from "axios";

export default {
  state: {
    registeredUser: null,
    loggedInUser:
      localStorage.getItem("userInfo") != null
        ? JSON.parse(localStorage.getItem("userInfo"))
        : null,
    loading: false,
    error: null,
  },
  getters: {
    registeredUser: (state) => state.registeredUser,
    loggedInUser: (state) => state.loggedInUser,
    loading: (state) => state.loading,
    error: (state) => state.error,
  },
  mutations: {
    setRegisteredUser(state, data) {
      state.registeredUser = data;
    },
    setLoggedInUser(state, data) {
      state.loggedInUser = data;
    },
    setLogout(state) {
      state.loggedInUser = null;
      state.loading = false;
      state.error = null;
    },
    setLoading(state, data) {
      state.loading = data;
      state.error = null;
    },
    clearLoading(state) {
      state.loading = false;
    },
    setError(state, data) {
      state.error = data;
      state.loggedInUser = null;
      state.loading = false;
    },
    clearError(state) {
      state.error = null;
    },
  },
  actions: {
    login({ commit }, data) {
      commit("setLoading", true);
      commit("clearError");

      axios
        .post("auth/login/", data)
        .then((resp) => {
          if (resp && resp.status === 200) {
            const userInfo = { ...resp.data };
            localStorage.setItem("userInfo", JSON.stringify(userInfo));

            axios.defaults.headers.common[
              "Authorization"
            ] = `JWT ${userInfo.access}`;

            commit("clearLoading", false);
            commit("setLoggedInUser", userInfo);
          }
        })
        .catch((error) => {
          if (
            error.response &&
            error.response.data &&
            error.response.data.message
          )
            commit("setError", error.response.data);

          if (
            error.response &&
            error.response.data &&
            error.response.data.non_field_errors
          )
            commit("setError", {
              message: error.response.data.non_field_errors[0],
            });

          commit("clearLoading", false);
          localStorage.removeItem("userInfo");
        });
    },
    register({ commit }, data) {
      commit("setLoading", true);
      commit("clearError");

      axios
        .post("auth/register/", data)
        .then((resp) => {
          if (resp && resp.status === 200) {
            commit("setRegisteredUser", resp.data);
          }

          commit("clearLoading", false);
        })
        .catch((error) => {
          if (
            error &&
            error.response &&
            error.response.data &&
            error.response.data.email
          )
            commit("setError", { message: error.response.data.email[0] });

          commit("clearLoading", false);
          localStorage.removeItem("userInfo");
        });
    },
    forgot({ commit }, data) {
      commit("setLoading", true);
      commit("clearError");

      axios
        .post("auth/forgot/password/", data)
        .then((resp) => {
          if (resp && resp.status === 200) {
            if (resp.data && resp.data.detail) {
              commit("setRegisteredUser", { message: resp.data.detail });
            }
          }

          commit("clearLoading", false);
        })
        .catch((error) => {
          if (
            error &&
            error.response &&
            error.response.data &&
            error.response.data.email
          )
            commit("setError", { message: error.response.data.email[0] });

          commit("clearLoading", false);
          localStorage.removeItem("userInfo");
        });
    },
    reset({ commit }, data) {
      commit("setLoading", true);
      commit("clearError");

      axios
        .post("auth/forgot/password/confirm/", data)
        .then((resp) => {
          if (resp && resp.status === 200) {
            if (resp.data && resp.data.detail) {
              commit("setRegisteredUser", { message: resp.data.detail });
            }
          }

          commit("clearLoading", false);
        })
        .catch((error) => {
          if (
            error.response &&
            error.response.data &&
            error.response.data.token &&
            error.response.data.token[0]
          )
            commit("setError", { message: error.response.data.token[0] });

          if (
            error.response &&
            error.response.data &&
            error.response.data.password1 &&
            error.response.data.password1[0]
          )
            commit("setError", { message: error.response.data.password1[0] });

          commit("clearLoading", false);
          localStorage.removeItem("userInfo");
        });
    },
    logout({ commit }) {
      localStorage.removeItem("userInfo");
      commit("setLogout");
    },
  },
};
