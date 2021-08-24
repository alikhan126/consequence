<template>
  <div class="main-content" v-if="!loading">
    <b-row>
      <b-col lg="12" xl="12" md="12">
        <div class="d-flex justify-content-between">
          <div class="d-flex align-items-center mb-4">
            <div class="mr-3 page-title">
              <h3 class="font-weight-bold m-0">Bank Account</h3>
            </div>
          </div>
        </div>
        <div class="mb-20">
          <Table title="Incomplete" />
        </div>

       <!--  <div class="delta-dental-tab">
          <b-tabs content-class="mt-1">
            <b-tab
              title="Incomplete"
              :active="getSelectedTab === 'incomplete'"
              @click="setTab('incomplete')"
            >
              <
            </b-tab>
            <b-tab
              title="Pending"
              :active="getSelectedTab === 'pending'"
              @click="setTab('pending')"
            >
              <div class="mb-20">
                <Table title="Pending" />
              </div>
            </b-tab>
            <b-tab
              title="Completed"
              :active="getSelectedTab === 'completed'"
              @click="setTab('completed')"
            >
              <div class="mb-20">
                <Table title="Completed" />
              </div>
            </b-tab>
            <b-tab
              title="Refunded"
              :active="getSelectedTab === 'refunded'"
              @click="setTab('refunded')"
            >
              <div class="mb-20">
                <Table title="Refunded" />
              </div>
            </b-tab>
            <b-tab
              title="Failed"
              :active="getSelectedTab === 'overDue'"
              @click="setTab('overDue')"
            >
              <div class="mb-20">
                <Table title="Overdue" />
              </div>
            </b-tab>
          </b-tabs>
        </div> -->
      </b-col>
    </b-row>
  </div>
  <Loader v-else />
</template>
<script>
import { mapActions, mapGetters } from "vuex";
import Loader from "../../../components/loader/loader";
import Table from "./table";

export default {
  components: {
    Table,
    Loader,
  },
  data() {
    return {
      loading: false,
    };
  },
  computed: {
    ...mapGetters([
      "getSelectedTab",
      "loggedInUser",
    ]),
  },
  watch: {
    getSelectedLocation(val) {
      if (val) {
        this.fetch();
      }
    },
    cardCharged(val) {
      if (val) {
        if (val.data) {
          this.makeToast("success", val.data);
          this.fetch();
        }
      }
    },
    errors(val) {
      if (val) {
        if (val.message) this.makeToast("danger", val.message);

        if (val.data) {
          this.makeToast("danger", val.data);
        }

        if (Array.isArray(val)) {
          val.forEach((v) => this.makeToast("danger", v.detail));
        }

        setTimeout(() => {
          this.fetch();
        }, 1000);
      }
    },
    reminderSent(val) {
      if (val) {
        this.makeToast("success", val.data);
      }
    },
  },
  methods: {
    ...mapActions(["setTab", "fetchPayments"]),

    async fetch() {
      this.loading = true;

      if (this.getSelectedLocation && this.getSelectedLocation.id)
        await this.fetchPayments(this.getSelectedLocation.id);

      setTimeout(() => {
        this.loading = false;
      }, 500);
    },

    makeToast(variant = null, msg) {
      this.$bvToast.toast(msg, {
        title: ` ${variant || "default"}`,
        variant: variant,
        solid: true,
      });
    },
  },
  mounted() {
    // if (this.loggedInUser && this.loggedInUser.role !== 1)
    //   return this.$router.push("/app/claims");

    this.setTab("incomplete");
    this.fetch();
  },
};
</script>
<style>
.delta-dental-tab span {
  color: #9badbf;
  font-weight: normal;
}
.delta-dental-tab span.active-tab {
  color: #355677;
}
.huddle-tab {
  background-color: #eaf4fb;
  padding: 20px;
  border-radius: 10px;
}
.tabs .nav-tabs {
  border: 0;
}
.tabs .nav-tabs .nav-item .nav-link {
  border: 0;
  background-color: transparent;
  position: relative;
  font-weight: bold;
  color: #05070b;
  padding: 10px 10px 5px;
}
.tabs .nav-tabs .nav-item .nav-link.active:before {
  content: "";
  position: absolute;
  right: 0;
  bottom: 0;
  left: 0;
  width: 20px;
  height: 2px;
  background-color: #6cdcd4;
  margin: 0 auto;
}
.tabs .nav-tabs .nav-item .nav-link.active {
  color: #6cdcd4;
  border: 0;
  background-color: transparent;
}

#notes-view .form-control-plaintext,
#appointment-location-view .form-control-plaintext {
  border: 2px solid #e5f4f8;
  border-radius: 5px;
  border-width: 1px;
}
#add-delta-dental .b-form-datepicker.focus {
  box-shadow: none;
}
#add-delta-dental .b-form-datepicker .btn {
  padding: 7px 10px;
}
</style>