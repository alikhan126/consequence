<template>
  <div v-if="!getLoading">
    <div class="main-content table-list">
      <div class="mb-3 page-title">
        <h3 class="font-weight-bold m-0">Appointments</h3>
      </div>
      <Table />
    </div>

    <b-modal id="add-appointment" size="lg" hide-header hide-footer>
      <div class="location-tab">
        <h6 class="title"><span>Appointment Information</span></h6>
        <div class="form-row">
          <div class="col-md-12">
            <b-form-group class="mb-3">
              <div class="form-row">
                <div class="col-md-12">
                  <label>Name <span class="required">*</span></label>
                  <b-form-input type="text" required />
                </div>
              </div>
            </b-form-group>
            <b-form-group>
              <div class="form-row">
                <div class="col-md-12">
                  <label>Address <span class="required">*</span></label>
                  <b-form-input type="text" class="mb-2" required />
                  <b-form-input type="text" required />
                </div>
              </div>
            </b-form-group>
          </div>
        </div>
        <div class="row">
          <div class="col-md-6">
            <b-form-group>
              <label>City <span class="required">*</span></label>
              <b-form-input type="text" required />
            </b-form-group>
          </div>
          <div class="col-md-3">
            <b-form-group>
              <label>State <span class="required">*</span></label>
              <b-dropdown class="state-dropdown" text="UT">
                <b-dropdown-item>UT</b-dropdown-item>
                <b-dropdown-item>BT</b-dropdown-item>
              </b-dropdown>
            </b-form-group>
          </div>
          <div class="col-md-3">
            <b-form-group>
              <label>Zip Code <span class="required">*</span></label>
              <b-form-input type="text" required />
            </b-form-group>
          </div>
        </div>
        <div class="row">
          <div class="col-md-6">
            <b-form-group>
              <label>Phone number <span class="required">*</span></label>
              <b-form-input type="text" required />
            </b-form-group>
          </div>
          <div class="col-md-6">
            <b-form-group>
              <label>Email</label>
              <b-form-input type="email" required />
            </b-form-group>
          </div>
        </div>
        <div class="row">
          <div class="col-md-6 offset-md-6"></div>
        </div>
        <div class="row">
          <div class="col-md-12">
            <div class="form-btn">
              <b-button variant="primary">Save</b-button>
              <b-button variant="outline-primary">Cancel</b-button>
            </div>
          </div>
        </div>
      </div>
    </b-modal>
  </div>
  <Loader v-else />
</template>
<style scoped>
.title {
  position: relative;
  font-weight: bold;
}
.title::before {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  background-color: #ddd;
  top: 50%;
  height: 1px;
}
.title span {
  background-color: #fff;
  position: relative;
  z-index: 1;
  padding-right: 5px;
}
.image-upload img {
  margin-bottom: 10px;
  width: 100px;
  height: 100px;
  object-fit: cover;
}
.location-tab .form-btn {
  margin: 20px -15px -15px;
  background-color: #e5f4f8;
  padding: 15px;
}
.location-tab .form-btn .btn + .btn {
  margin-left: 10px;
}
.trans-userId i {
  font-size: 16px;
  margin-left: 5px;
}
</style>
<script>
import { mapGetters, mapActions } from "vuex";
import Loader from "../../../components/loader/loader";
import Table from "./table";

// const STORAGE_KEY = 'invoice';
export default {
  data() {
    return {};
  },
  components: { Loader, Table },
  computed: mapGetters(["getLoading"]),
  mounted() {
    this.setLoading(true);
    setTimeout(() => {
      this.setLoading(false);
    }, 1000);
  },
  methods: {
    ...mapActions(["setLoading"]),
  },
};
</script>