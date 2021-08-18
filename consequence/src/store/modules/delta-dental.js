const defaultDeltaDentalForm = {
  first_name: "",
  last_name: "",
  appointment_date: new Date(),
  appointment_loc: "",
  ins_policy: "",
  status: "",
  email: "",
  phone: "",
  charge_date: new Date(),
  payment_amount: 0,
  notes: "",
}
const state = {
  rows: {
    pending: [
      {
        id: 1,
        first_name: "Devin",
        last_name: "Picciolini",
        name: "Devin Picciolini",
        appointment_date: "2021-05-18",
        charge_date: "2021-06-17",
        payment_amount: 150,
        notes: "This is the sample text to display!",
        appointment_loc: "test appointment location 123",
        ins_policy: "987358ijhbg",
        status: "Pending",
        email: "hello@honeydu.io",
        phone: "8153028613",
        customer_card: []
      }
    ],
    completed: [
      {
        id: "2",
        first_name: "Picciolini",
        last_name: "Devin",
        name: "Devin Picciolini",
        appointment_date: "2021-05-18",
        charge_date: "2021-06-17",
        payment_amount: "$250",
        notes: "This is the sample text to display!",
        appointment_loc: "test appointment location 456",
        ins_policy: "987358ijhbg",
        status: "Completed",
        email: "hello@honeydu.io",
        phone: "9925012345",
        customer_card: [
          {
            id: 1,
            cvv: "555",
            expiry_date: "12/22",
            card_number: 4646464646,
            postal: 394101,
            holder_name: "Test Holder",
            country: "India",
            first_name: "Test Name",
            last_name: "Bali",
            card_brand: "VISA"
          }
        ]
      }
    ],
    overDue: [
      {
        id: "3",
        first_name: "Devin",
        last_name: "Picciolini",
        name: "Devin Picciolini",
        appointment_date: "2021-05-18",
        charge_date: "2021-06-17",
        payment_amount: "$150",
        notes: "This is the sample text to display!",
        appointment_loc: "test appointment location 789",
        ins_policy: "987358ijhbg",
        status: "Over Due",
        email: "hello@honeydu.io",
        phone: "8153028613",
        customer_card: []
      }
    ]
  },
  selectedTab: "pending",
  selectedRecord: null,
  addRecord: "",
  defaultDeltaDentalForm: { ...defaultDeltaDentalForm },
  deltaDentalForm: { ...defaultDeltaDentalForm },
};

const getters = {
  deltaDentalList: state => state.rows[state.selectedTab],
  getAddRecord: state => state.addRecord,
  getSelectedTab: state => state.selectedTab,
  getSelectedRecord: state => state.selectedRecord,
  getDeltaDentalForm: state => state.deltaDentalForm,
};

const actions = {
  addRecord({ commit }, data) {
    commit("ADD_RECORD", data);
  },
  setTab({ commit }, data) {
    commit("SET_TAB", data);
  },
  setRecord({ commit }, data) {
    commit("SET_RECORD", data);
  },
  removeRecord({ commit }, data) {
    commit("REMOVE_RECORD", data);
  },
  saveRecord({ commit }, data) {
    commit("SAVE_RECORD", data);
  },
  updateRecord({ commit }, data) {
    commit("UPDATE_RECORD", data);
  },
  saveCard({ commit }, data) {
    commit("SAVE_CARD", data);
  },
  removeCard({ commit }, data) {
    commit("REMOVE_CARD", data);
  },
  setDeltaDentalForm({ commit }, data) {
    commit("SET_DELTA_DENTAL_FORM", data)
  },
  setDefaultDeltaDentalForm({ commit }, data) {
    commit("SET_DEFAULT_DELTA_DENTAL_FORM", data)
  }
};

const mutations = {
  ADD_RECORD(state, data) {
    if (state.selectedTab !== "") {
      state.rows[state.selectedTab].push(data);
      state.addRecord = data;
    }
  },
  SET_TAB(state, data) {
    state.selectedTab = data;
  },
  SET_RECORD(state, data) {
    state.selectedRecord = data;
  },
  REMOVE_RECORD(state, data) {
    if (state.selectedTab !== "" && data.id) {
      const findRowIndex = state.rows[state.selectedTab].findIndex(({ id }) => id === data.id)
      if (findRowIndex > -1) {
        state.rows[state.selectedTab].splice(findRowIndex, 1)
        state.selectedRecord = null
      }
    }
  },
  UPDATE_RECORD(state, data) {
    if (state.selectedTab !== "") {
      const findRowIndex = state.rows[state.selectedTab].findIndex(({ id }) => id === state.selectedRecord && state.selectedRecord.id)
      if (findRowIndex > -1) {
        state.rows[state.selectedTab][findRowIndex] = data
      }
    }
  },
  SAVE_RECORD(state, data) {
    if (state.selectedTab !== "") {
      state.rows[state.selectedTab].push({ ...data, id: state.rows[state.selectedTab].length + 1 })
    }
  },
  SAVE_CARD(state, data) {
    if (state.selectedTab !== "" && state.selectedRecord) {
      const findRow = state.rows[state.selectedTab].find(({ id }) => id === state.selectedRecord.id)
      if (findRow) {
        findRow.customer_card.push({ ...data, id: findRow.customer_card && findRow.customer_card.length + 1, card_brand: "VISA" })
      }
    }
  },
  REMOVE_CARD(state, data) {
    if (state.selectedTab !== "" && state.selectedRecord) {
      const findRowIndex = state.rows[state.selectedTab].findIndex(({ id }) => id === state.selectedRecord.id)
      if (findRowIndex > -1) {
        const findCardIndex = state.rows[state.selectedTab][findRowIndex].customer_card.findIndex(({ id }) => id === data.id)
        if (findCardIndex > -1) {
          state.rows[state.selectedTab][findRowIndex].customer_card.splice(findCardIndex, 1)
          state.selectedRecord = state.rows[state.selectedTab][findRowIndex]
        }
      }
    }
  },
  SET_DELTA_DENTAL_FORM(state, data) {
    state.deltaDentalForm = data;
  },
  SET_DEFAULT_DELTA_DENTAL_FORM(state) {
    state.deltaDentalForm = defaultDeltaDentalForm;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};
