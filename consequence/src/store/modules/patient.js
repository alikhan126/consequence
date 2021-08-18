const defaultPatientForm = {
    first_name: "",
    middle_name: "",
    last_name: "",
    email_address: "",
    date_of_birth: null,
    gender: null,
    nick_name: "",
    phone: "",
    cell: "",
    foreign_id: "",
    guardian: "",
    ssn: "",
    home_office: "",
    other_notes: "",
    insurance_policy: ""
}
const state = {
    rows: [
        {
            id: 1,
            name: "Devin Picciolini",
            first_name: "Devin",
            middle_name: "",
            last_name: "Picciolini",
            email_address: "devin@honeydu.io",
            phone: "8153028613",
            date_of_birth: new Date(new Date().setFullYear(1998)),
            gender: "Male",
            nick_name: "MM",
            cell: "",
            foreign_id: "",
            guardian: "",
            ssn: "123",
            home_office: "",
            other_notes: "This is the sample text to display!",
            insurance_policy: "New Policy",
            customer_card: []
        },
        {
            id: "2",
            name: "Picciolini Devin",
            first_name: "Picciolini",
            middle_name: "",
            last_name: "Devin",
            email_address: "picciolini@devin.io",
            phone: "8153028613",
            date_of_birth: new Date(new Date().setFullYear(1998)),
            gender: "Male",
            nick_name: "MM",
            cell: "",
            foreign_id: "",
            guardian: "",
            ssn: "123",
            home_office: "",
            other_notes: "This is the sample text to display!",
            insurance_policy: "New Policy",
            customer_card: [
                {
                    id: 1,
                    cvv: "555",
                    expiry_date: "12/22",
                    card_number: 4646464646,
                    postal: 394101,
                    card_brand: "VISA"
                }
            ]
        }
    ],
    selectedRecord: null,
    patientsList: [
        {
            id: 1,
            doctorId: 1,
            onCall: true,
            first_name: "Patient 1",
            last_name: "Demo",
            startTime: new Date(new Date().setHours(2)),
            endTime: new Date(new Date().setHours(5)),
            dob: new Date(1978, 2, 9)
        },
        {
            id: 2,
            doctorId: 2,
            first_name: "Patient 2",
            last_name: "Demo",
            startTime: new Date(new Date().setHours(8)),
            endTime: new Date(new Date().setHours(10)),
            dob: new Date(1984, 2, 9)
        },
        {
            id: 3,
            doctorId: 3,
            first_name: "Patient 3",
            last_name: "Demo",
            startTime: new Date(new Date().setHours(11)),
            endTime: new Date(new Date().setHours(12)),
            dob: new Date(1991, 2, 9)
        },
        {
            id: 4,
            doctorId: 4,
            onCall: true,
            first_name: "Patient 4",
            last_name: "Demo",
            startTime: new Date(new Date().setHours(15)),
            endTime: new Date(new Date().setHours(18)),
            dob: new Date(1989, 2, 9)
        },
        {
            id: 5,
            doctorId: 5,
            first_name: "Patient 5",
            last_name: "Demo",
            startTime: new Date(new Date().setHours(21)),
            endTime: new Date(new Date().setHours(23)),
            dob: new Date(1995, 2, 9)
        },
    ],
    patientData: {},
    patientForm: { ...defaultPatientForm }
};

const getters = {
    getPatientData: state => state.patientData,
    getPatientsList: state => state.patientsList,
    getActiveTabInPatientForm: state => state.activeTab,
    getPatientForm: state => state.patientForm,
    getSelectedPatient: state => state.selectedRecord,
    getPatients: state => state.rows,
};

const actions = {
    setPatientData({ commit }, data) {
        commit("SET_PATIENT_DATA", data);
    },
    setActiveTabInPatientForm({ commit }, data) {
        commit("SET_ACTIVE_TAB", data);
    },
    setRecord({ commit }, data) {
        commit("SET_RECORD", data);
    },
    savePatient({ commit }, data) {
        commit("SAVE_PATIENT", data);
    },
    savePatientCard({ commit }, data) {
        commit("SAVE_PATIENT_CARD", data);
    },
    updatePatient({ commit }, data) {
        commit("UPDATE_PATIENT", data);
    },
    removePatient({ commit }, data) {
        commit("REMOVE_PATIENT", data);
    },
    removePatientCard({ commit }, data) {
        commit("REMOVE_PATIENT_CARD", data);
    },
    setDefaultPatientForm({ commit }, data) {
        commit("SET_DEFAULT_PATIENT_FORM", data)
    },
    setPatientForm({ commit }, data) {
        commit("SET_PATIENT_FORM", data)
    }
};

const mutations = {
    SET_PATIENT_DATA(state, data) {
        state.patientData = { ...state.patientData, ...data }
    },
    SET_ACTIVE_TAB(state, data) {
        state.activeTab = data
    },
    SET_RECORD(state, data) {
        state.selectedRecord = data;
    },
    SET_DEFAULT_PATIENT_FORM(state) {
        state.patientForm = defaultPatientForm;
    },
    SAVE_PATIENT(state, data) {
        const rowList = state.rows || []
        rowList.push(data)
        state.rows = rowList
    },
    UPDATE_PATIENT(state, data) {
        const patientIndex = state.rows.findIndex((p) => p.id === data.id)
        if (patientIndex > -1) {
            state.rows[patientIndex] = { ...data, ...state.rows[patientIndex] }
        }
    },
    REMOVE_PATIENT(state, data) {
        const patientIndex = state.rows.findIndex((p) => p.id === data.id)
        if (patientIndex > -1) {
            state.rows.splice(patientIndex, 1)
        }
    },
    SET_PATIENT_FORM(state, data) {
        state.patientForm = data;
    },
    SAVE_PATIENT_CARD(state, data) {
        if (state.selectedRecord) {
            const findRow = state.rows.find(({ id }) => id === state.selectedRecord.id)
            if (findRow) {
                findRow.customer_card.push({ ...data, id: findRow.customer_card && findRow.customer_card.length + 1, card_brand: "VISA" })
            }
        }
    },
    REMOVE_PATIENT_CARD(state, data) {
        if (state.selectedRecord) {
            const findRowIndex = state.rows.findIndex(({ id }) => id === state.selectedRecord.id)
            if (findRowIndex > -1) {
                const findCardIndex = state.rows[findRowIndex].customer_card.findIndex(({ id }) => id === data.id)
                if (findCardIndex > -1) {
                    state.rows[findRowIndex].customer_card.splice(findCardIndex, 1)
                    state.selectedRecord = state.rows[findRowIndex]
                }
            }
        }
    },
};

export default {
    state,
    getters,
    actions,
    mutations
};
