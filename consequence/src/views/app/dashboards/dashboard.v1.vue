<template>
  <!-- ============ Body content start ============= -->
  <div class="main-content">
    <b-row>
      <b-col lg="12" xl="12" md="12">
        <!--  <b-card header="Daily Huddle" header-bg-variant="transparent">-->
        <div class="d-flex justify-content-between">
          <div class="d-flex align-items-center mb-4">
            <div class="mr-3 page-title">
              <h3 class="font-weight-bold m-0">Dashboard</h3>
            </div>
          </div>
        </div>
      </b-col>
    </b-row>

    <div class="row">
      <div class="col-lg-12 col-xl-12 col-md-12">
        <div class="row">
          <div class="col-lg-6 col-md-6">
            <div class="card card-chart-bottom o-hidden mb-30">
              <div class="card-body pb-0">
                <div class="text-muted" style="font-size: 40px">🔥</div>
                <p class="text-primary text-24 m-0">40250</p>
              </div>
              <div class="chart-wrapper" style="height: 260px">
                <v-chart :options="echart1" :autoresize="true"></v-chart>
              </div>
            </div>
          </div>

          <div class="col-lg-6 col-md-6">
            <div class="card card-chart-bottom o-hidden mb-30">
              <div class="card-body pb-0">
                <div class="text-muted" style="font-size: 40px">🧊</div>
                <p class="text-warning text-24 m-0">10250</p>
              </div>
              <div class="chart-wrapper" style="height: 260px">
                <v-chart :options="echart2" :autoresize="true"></v-chart>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="col-md-12">
        <div class="card mb-30">
          <div class="card-body p-0">
            <h5 class="card-title border-bottom p-3 mb-2">Recent Orders</h5>

            <vue-good-table
              :columns="columns"
              :line-numbers="false"
              styleClass="order-table vgt-table"
              :rows="rows"
            >
            </vue-good-table>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- ============ Body content End ============= -->
</template>
<script>
import { echartBar, echartPie } from "@/data/echarts";

import { echart1, echart2, echart3 } from "@/data/dashboard1";

export default {
  metaInfo: {
    // if no subcomponents specify a metaInfo.title, this title will be used
    title: "Dashboard v1",
  },
  data() {
    return {
      echartBar,
      echartPie,
      echart1,
      echart2,
      echart3,
      columns: [
        {
          label: "Order Id",
          field: "id",
          thClass: "text-left pl-3",
          tdClass: "text-left pl-3",
        },
        {
          label: "Buyer Name",
          field: "name",
          thClass: "text-left",
          tdClass: "text-left",
        },
        {
          label: "Product",
          field: "img",
          html: true,
          thClass: "text-left",
          tdClass: "text-left",
        },
        {
          label: "Status",
          field: "span",
          html: true,
          thClass: "text-left",
          tdClass: "text-left",
        },

        {
          label: "Shipping Cost",
          field: "score",

          // html:true,
          type: "percentage",
          thClass: "text-left",
          tdClass: "text-left",
        },
        {
          label: "Date",
          field: "createdAt",
          type: "date",
          dateInputFormat: "yyyy-mm-dd",
          dateOutputFormat: "mmm Do yy",
          thClass: "text-left",
          tdClass: "text-left",
        },
        {
          label: "Action",
          field: "action",
          html: true,
          thClass: "text-left",
          tdClass: "text-left",
        },
      ],
      rows: [
        {
          id: 1,
          name: "John",
          img:
            '<img src="' +
            require("@/assets/images/products/iphone-1.jpg") +
            '" class="rounded-circle avatar-sm" alt=""> <img src="' +
            require("@/assets/images/products/iphone-2.jpg") +
            '" class="rounded-circle avatar-sm" alt="">',
          span: '<span class="badge badge-pill badge-outline-primary p-2 ">Delivered</span>',
          createdAt: "2019-10-31 ",
          score: 0.03343,
          action:
            '<button class=" btn btn-outline-primary text-black btn-rounded">View</button>',
        },
        {
          id: 2,
          name: "Jane",
          img:
            '<img src="' +
            require("@/assets/images/products/headphone-1.jpg") +
            '" class="rounded-circle avatar-sm" alt=""> <img src="' +
            require("@/assets/images/products/headphone-2.jpg") +
            '" class="rounded-circle avatar-sm" alt="">',
          span: '<span class="badge badge-pill badge-outline-danger p-2">Shipped</span>',
          createdAt: "2011-10-31",
          score: 0.03343,
          action:
            '<button class=" btn btn-outline-primary text-black btn-rounded">View</button>',
        },
        {
          id: 3,
          name: "Susan",
          img:
            '<img src="' +
            require("@/assets/images/products/headphone-3.jpg") +
            '" class="rounded-circle avatar-sm" alt=""> <img src="' +
            require("@/assets/images/products/headphone-4.jpg") +
            '" class="rounded-circle avatar-sm" alt="">',
          span: '<span class="badge badge-pill badge-outline-success p-2 ">Delivered</span>',
          createdAt: "2011-10-30",
          score: 0.03343,
          action:
            '<button class=" btn btn-outline-primary text-black btn-rounded">View</button>',
        },
        {
          id: 4,
          name: "Chris",
          img:
            '<img src="' +
            require("@/assets/images/products/speaker-1.jpg") +
            '" class="rounded-circle avatar-sm" alt=""> <img src="' +
            require("@/assets/images/products/speaker-2.jpg") +
            '" class="rounded-circle avatar-sm" alt="">',
          span: '<span class="badge badge-pill badge-outline-primary p-2">Pending</span>',
          createdAt: "2011-10-11",
          score: 0.03343,
          action:
            '<button class=" btn btn-outline-primary text-black btn-rounded">View</button>',
        },
        {
          id: 5,
          name: "Dan",
          img:
            '<img src="' +
            require("@/assets/images/products/watch-1.jpg") +
            '" class="rounded-circle avatar-sm" alt=""> <img src="' +
            require("@/assets/images/products/watch-2.jpg") +
            '" class="rounded-circle avatar-sm" alt="">',
          span: '<span class="badge badge-pill badge-outline-info p-2">Processing</span>',
          createdAt: "2011-10-21",
          score: 0.03343,
          action:
            '<button class=" btn btn-outline-primary text-black btn-rounded">View</button>',
        },
        {
          id: 6,
          name: "John",
          img:
            '<img src="' +
            require("@/assets/images/products/speaker-1.jpg") +
            '" class="rounded-circle avatar-sm" alt=""> <img src="' +
            require("@/assets/images/products/speaker-2.jpg") +
            '" class="rounded-circle avatar-sm" alt="">',
          span: '<span class="badge badge-pill badge-outline-success p-2 ">Delivered</span>',
          createdAt: "2011-10-31",
          score: 0.03343,
          action:
            '<button class=" btn btn-outline-primary text-black btn-rounded">View</button>',
        },
        {
          id: 7,
          name: "John",
          img:
            '<img src="' +
            require("@/assets/images/products/headphone-3.jpg") +
            '" class="rounded-circle avatar-sm" alt=""> <img src="' +
            require("@/assets/images/products/headphone-4.jpg") +
            '" class="rounded-circle avatar-sm" alt="">',
          span: '<span class="badge badge-pill badge-outline-info p-2 ">Pending</span>',
          createdAt: "2019-10-31 ",
          score: 0.03343,
          action:
            '<button class=" btn btn-outline-primary text-black btn-rounded">View</button>',
        },
        {
          id: 8,
          name: "Jane",
          img:
            '<img src="' +
            require("@/assets/images/products/iphone-1.jpg") +
            '" class="rounded-circle avatar-sm" alt=""> <img src="' +
            require("@/assets/images/products/iphone-1.jpg") +
            '" class="rounded-circle avatar-sm" alt="">',
          span: '<span class="badge badge-pill badge-outline-danger p-2">Shipped</span>',
          createdAt: "2011-10-31",
          score: 0.03343,
          action:
            '<button class=" btn btn-outline-primary text-black btn-rounded">View</button>',
        },
      ],
    };
  },
};
</script>
<style>
.echarts {
  width: 100%;
  height: 100%;
}
</style>
