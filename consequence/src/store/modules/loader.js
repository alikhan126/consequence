const state = {
    loading: false,
};

const getters = {
    getLoading: state => state.loading
};

const actions = {
    setLoading({ commit }, id) {
        commit("SET_LOADING", id);
    }
};

const mutations = {
    SET_LOADING(state, data) {
        state.loading = data;
    }
};

export default {
    state,
    getters,
    actions,
    mutations
};
