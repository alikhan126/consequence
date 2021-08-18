import axios from "axios";

const state = {};
const getters = {};
const mutations = {};

const actions = {
  fetchUsers({ commit }) {
    return new Promise((resolve, reject) => {
      axios
        .get(`auth/users/${id}`)
        .then((resp) => resolve(resp.data))
        .catch((err) => reject(err));
    });
  },


  updateUser({ commit }, { id, firstname, lastname, email }) {
    return new Promise((resolve, reject) => {
      axios
        .put(`users/${id}`, {
          firstname,
          lastname,
        })
        .then((resp) => resolve(resp.data))
        .catch((err) => reject(err));
    });
  },

};

export default {
  state,
  getters,
  actions,
  mutations,
};