<template>
  <div class="main-content" v-if="!getLoading">
    <!-- <breadcumb :page="'Dashboard'" :folder="'Version 1'" /> -->
    <b-row>
      <b-col lg="9" md="8">
        <!--  <b-card header="Daily Huddle" header-bg-variant="transparent">-->
        <div class="mb-3 page-title">
          <h3 class="font-weight-bold m-0">Schedule</h3>
        </div>

        <div class="schedule-vue-sample">
          <div class="col-md-12 control-section">
            <div class="content-wrapper schedule-container without-date-header">
              <ejs-schedule
                v-if="show"
                id="Schedule"
                ref="ScheduleObj"
                :height="calenderHieght"
                cssClass="quick-info-template"
                :selectedDate="selectedDate"
                :eventSettings="eventSettings"
                :eventRendered="onEventRendered"
                :group="group"
                :showTimeIndicator="showTimeIndicator"
                :currentView="currentView"
                :actionBegin="onActionBegin"
                :actionComplete="onActionComplete"
                :cellClick="onCellClick"
                :eventClick="onEventClick"
                :popupOpen="onPopupOpen"
                :navigating="onNavigating"
                :quickInfoTemplates="quickInfoTemplates"
              >
                <e-views>
                  <e-view
                    option="Day"
                    :allowVirtualScrolling="virtualScroll"
                  ></e-view>
                  <!-- <e-view option="Week"></e-view>
                  <e-view option="Month"></e-view>
                  <e-view option="Agenda"></e-view> -->
                </e-views>
                <e-resources>
                  <e-resource
                    field="DoctorId"
                    title="Doctor"
                    name="Doctors"
                    :allowMultiple="allowMultiple"
                    :dataSource="resourceDataSource"
                    textField="Text"
                    idField="Id"
                    groupIDField="DoctorId"
                    colorField="Color"
                  >
                  </e-resource>
                </e-resources>
              </ejs-schedule>
            </div>
          </div>
        </div>
      </b-col>
      <b-col lg="3" md="4">
        <div class="mb-3 page-title">
          <h3 class="font-weight-bold m-0">Appointment Requests</h3>
        </div>
        <div class="appointment-requests-tab">
          <b-tabs content-class="mt-1">
            <b-tab title="ASAP">
              <div class="appointment-list">
                <div
                  class="appointment-card"
                  v-for="num in [1, 2, 3]"
                  :key="num"
                >
                  <div class="appointment-date-time">
                    <span>Mar 19, 2021</span>
                    <span>5:00 PM - 6:00 PM</span>
                  </div>
                  <div class="appointment-title">He - Ryan Smith</div>
                  <div class="contact-info">
                    <span>melissa.luvisi@gmail.com</span>
                    <span>(310)487-4291</span>
                  </div>
                  <div class="submitted-date">
                    <span>Submitted on 3/17/21</span>
                    <i class="fa fa-calendar-check-o"></i>
                  </div>
                </div>
              </div>
            </b-tab>
            <b-tab title="Pinboard" active>
              <div class="appointment-list">
                <div
                  class="appointment-card"
                  v-for="num in [1, 2, 3]"
                  :key="num"
                >
                  <div class="appointment-date-time mb-2">
                    <i class="fa fa-thumb-tack pin-icon"></i>
                    <span> Michelle Taylor Lagunas</span>
                  </div>
                  <div class="appointment-title">
                    <p>Mar 19, 2021</p>
                    <p>Consult for braces</p>
                    <p>Consult, ITERO</p>
                  </div>
                  <div class="submitted-date">
                    <span>Show Production</span>
                  </div>
                </div>
              </div>
            </b-tab>
          </b-tabs>
        </div>
      </b-col>
    </b-row>
  </div>
  <Loader v-else />
</template>
<style>
.schedule-vue-sample .quick-info-template .quick-info-title {
  font-weight: 500;
  font-size: 16px;
  letter-spacing: 0.48px;
  height: 22px;
}

.schedule-vue-sample .quick-info-template .duration-text {
  font-size: 11px;
  letter-spacing: 0.33px;
  height: 14px;
}

.schedule-vue-sample .quick-info-template .content-area {
  margin: 0;
  padding: 10px;
  width: auto;
}
.schedule-vue-sample .quick-info-template .cell-footer.e-btn {
  background-color: #ffffff;
  border-color: #878787;
  color: #878787;
}

.schedule-vue-sample .quick-info-template .cell-footer {
  padding-top: 10px;
}

.schedule-vue-sample
  .quick-info-template
  .e-quick-popup-wrapper
  .e-cell-popup
  .e-popup-content {
  padding: 0 14px;
}

.schedule-vue-sample
  .quick-info-template
  .e-quick-popup-wrapper
  .e-event-popup
  .e-popup-footer {
  display: block;
}

.schedule-vue-sample
  .quick-info-template
  .e-quick-popup-wrapper
  .e-popup-footer
  button:first-child {
  margin-right: 5px;
}

.appointment-list {
  height: -moz-calc(100vh - 200px);
  height: -webkit-calc(100vh - 200px);
  height: calc(100vh - 200px);
  overflow-y: auto;
}
.appointment-card {
  background-color: #fff;
  border-radius: 10px;
  padding: 15px;
  margin-bottom: 40px;
  box-shadow: 0 3px 10px rgb(0 0 0 / 5%);
}
.appointment-card:last-child {
  margin-bottom: 0;
}
.appointment-date-time span {
  color: #00c5b4;
  display: block;
  font-size: 16px;
}
.appointment-title {
  color: #12395f;
  font-weight: bold;
  font-size: 17px;
}
.appointment-title p {
  margin-bottom: 0;
  font-size: 14px;
}
.pin-icon {
  float: right;
  color: #d6d6d6;
  font-size: 20px !important;
}
.contact-info span {
  color: #c7cadd;
  display: block;
  font-size: 16px;
}
.contact-info {
  margin-top: 10px;
}
.submitted-date {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  margin-top: 15px;
  color: #c7cadd;
}
.submitted-date i {
  color: #00c5b4;
  font-size: 20px;
}
.appointment-requests-tab .tabs .nav-tabs .nav-item a {
  font-size: 16px;
  margin-left: 0px;
  margin-right: 30px;
}
.appointment-requests-tab .tabs .tab-content {
  padding: 0;
}
.tabs .nav-tabs {
  border: 0;
}
.tabs .nav-tabs .nav-item .nav-link {
  border: 0;
  background-color: transparent;
  position: relative;
  font-weight: bold;
  color: #8da1b5 !important;
  padding: 0;
  margin: 10px;
}
.tabs .nav-tabs .nav-item .nav-link:before {
  content: "";
  position: absolute;
  right: 0;
  bottom: 0;
  left: 0;
  width: 0;
  height: 1px !important;
  background-color: #6cdcd4;
  transition: all 0.5s ease-in-out;
}
.tabs .nav-tabs .nav-item .nav-link.active:before,
.tabs .nav-tabs .nav-item .nav-link:hover:before {
  width: 100%;
}
.tabs .nav-tabs .nav-item .nav-link.active,
.tabs .nav-tabs .nav-item .nav-link:hover {
  color: #6cdcd4 !important;
  border: 0;
  background-color: transparent;
}
.patient-info {
  display: flex;
  padding: 20px;
  box-shadow: 0px 4px 5px rgba(0, 0, 0, 0.05);
  border-radius: 10px;
}
.right {
  margin-left: auto;
}

.patient-img img {
  border-radius: 100%;
  max-width: 60px;
}

.patient-img {
  margin-right: 10px;
  float: left;
}
.patient-detail {
  overflow: hidden;
  margin-top: 10px;
}

.right p {
  margin: 0;
}

.right span {
  margin-bottom: 5px;
  display: block;
  font-weight: 600;
}

.patient-detail h6 {
  font-weight: 600;
  margin: 0;
  font-size: 20px;
}
.status-dropdown {
  display: inline-block;
  position: relative;
}
.status-dropdown label {
  display: block;
  position: absolute;
  top: 10px;
  margin: 0;
  z-index: 9;
  left: 10px;
}
.status-dropdown .dropdown-toggle.btn {
  padding: 0;
  background-color: #fafafa !important;
  border-radius: 10px;
  padding: 30px 50px 10px 10px;
  color: #05070b !important;
  font-size: 16px;
}
.status-dropdown .dropdown-toggle.btn:focus {
  box-shadow: none;
}
.status-dropdown .dropdown-toggle::after {
  content: normal;
}
.status-dropdown .dropdown-menu {
  min-width: 100%;
}
.status-dropdown:after {
  content: "\f107";
  font-family: "FontAwesome";
  border: 0;
  position: absolute;
  right: 10px;
  top: 50%;
  font-size: 24px;
  color: #05070b;
  font-weight: bold;
  -moz-transform: translateY(-50%);
  -webkit-transform: translateY(-50%);
  transform: translateY(-50%);
  pointer-events: none;
  z-index: 9;
}
.schedule-link,
.schedule-link:hover {
  margin-left: 20px;
  color: #00c5b4;
  text-decoration: underline;
}
.tx-planner-wrap {
  background-color: #fafafa;
  padding: 20px;
}
.search-procedure {
  position: relative;
}
.search-procedure i {
  position: absolute;
  right: 12px;
  top: 8px;
  font-size: 16px;
}
.required {
  color: #ac252b;
}
.tx-planner {
  color: #00c5b4;
  margin-top: 15px;
  display: block;
  cursor: pointer;
}
.selection-section {
  margin: 0;
  padding: 0;
}
.selection-section li {
  list-style: none;
  float: left;
  margin-right: 50px;
}
.selection-section li .checkbox {
  margin: 0;
}
.selection-section li .checkbox span {
  vertical-align: middle;
}
.form-group .patient-form-filed label {
  display: block;
  font-size: 16px;
  font-weight: bold;
  color: #05070b;
}
.patient-form-filed .b-dropdown,
.patient-form-filed .b-dropdown .btn,
.gender-dropdown.b-dropdown,
.gender-dropdown.b-dropdown .btn {
  width: 100%;
  text-align: left;
}
.time-icon {
  float: right;
  margin-top: 15px;
}
.patient-form-filed .dropdown-toggle,
.patient-form-filed input,
.patient-form-filed textarea {
  padding: 12px 20px;
  border-radius: 10px;
  height: auto;
}
.patient-form-filed .b-form-datepicker,
.patient-form-filed .b-form-btn-label-control.form-control.b-form-timepicker {
  border-radius: 10px;
}
.patient-form-filed .b-form-btn-label-control.form-control > .form-control {
  padding: 12px 20px;
  white-space: nowrap;
  min-height: auto;
  overflow: hidden;
  text-overflow: ellipsis;
}
.lenght-lebel {
  margin-left: 8px;
}
.patient-info-tabs .form-btn .btn {
  min-width: 150px;
}
.patient-info-tabs .btn + .btn {
  margin-left: 10px;
}
.patient-info-tabs .btn-link {
  padding-left: 0;
  padding-right: 0;
  min-width: auto;
}
.appt-form ul.dropdown-menu,
.gender-dropdown ul.dropdown-menu {
  min-width: auto;
  width: 100%;
}
.patient-info-tabs {
  padding-bottom: 61px;
}
.patient-form-button {
  position: absolute;
  background-color: #fff;
  left: 0;
  right: 0;
  bottom: 0;
}
.e-input-group::before,
.e-input-group::after {
  content: normal !important;
}
.e-multiselect.e-input-group.e-control-wrapper {
  border: 1px solid #9ca3af !important;
  border-radius: 5px;
}
.e-multiselect.e-input-group.e-control-wrapper.e-input-focus {
  border-width: 1px !important;
}
.e-multi-select-wrapper .e-searcher {
  margin-bottom: 0;
}
.e-control-wrapper .e-multi-select-wrapper {
  padding: 2px 10px;
  min-height: 32px;
}
.e-multi-select-wrapper .e-chips {
  margin-bottom: 0 !important;
  margin-top: 2px;
}
</style>

<script>
import Vue from "vue";
import { mapActions, mapGetters } from "vuex";
import fullscreen from "vue-fullscreen";
import { extend, Internationalization } from "@syncfusion/ej2-base";
import { ButtonPlugin } from "@syncfusion/ej2-vue-buttons";
import { DropDownListPlugin } from "@syncfusion/ej2-vue-dropdowns";
import { TextBoxPlugin } from "@syncfusion/ej2-vue-inputs";
import { TimePickerPlugin } from "@syncfusion/ej2-vue-calendars";
import {
  SchedulePlugin,
  Day,
  Agenda,
  Month,
  Week,
  Resize,
  DragAndDrop,
} from "@syncfusion/ej2-vue-schedule";
import * as moment from "moment";
import Loader from "../../../components/loader/loader";

Vue.use(SchedulePlugin);
Vue.use(ButtonPlugin);
Vue.use(DropDownListPlugin);
Vue.use(TextBoxPlugin);
Vue.use(TimePickerPlugin);
Vue.use(fullscreen);

const providerData = [
  { Name: "OP-1", Id: 1, Capacity: 20, Color: "#ea7a57", Type: "Conference" },
  { Name: "OP-2", Id: 2, Capacity: 7, Color: "#7fa900", Type: "Cabin" },
  { Name: "OP-3", Id: 3, Capacity: 5, Color: "#5978ee", Type: "Cabin" },
  { Name: "OP-4", Id: 4, Capacity: 15, Color: "#fec200", Type: "Conference" },
  {
    Name: "Other Office",
    Id: 5,
    Capacity: 10,
    Color: "#00bdae",
    Type: "Cabin",
  },
];
const appointmentData = [
  {
    Name: "Appointment-1",
    Id: 1,
    Capacity: 20,
    Color: "#ea7a57",
    Type: "Conference",
  },
  {
    Name: "Appointment-2",
    Id: 2,
    Capacity: 7,
    Color: "#7fa900",
    Type: "Cabin",
  },
  {
    Name: "Appointment-3",
    Id: 3,
    Capacity: 5,
    Color: "#5978ee",
    Type: "Cabin",
  },
  {
    Name: "Appointment-4",
    Id: 4,
    Capacity: 15,
    Color: "#fec200",
    Type: "Conference",
  },
  {
    Name: "Appointment-5",
    Id: 5,
    Capacity: 25,
    Color: "#df5286",
    Type: "Conference",
  },
];

var headerTemplateVue = Vue.component("headerTemplate", {
  template: `<div class="quick-info-header"></div>`,
  data: function () {
    return {
      intl: new Internationalization(),
      data: {},
    };
  },
  methods: {
    getHeaderStyles: function (data) {
      console.log(`data`, data);
      const scheduleObj =
        document.querySelector(".e-schedule").ej2_instances[0];
      console.log(`scheduleObj`, scheduleObj);
      const resources = scheduleObj.getResourceCollections().slice(-1)[0];
      console.log(`resources`, resources);
      const resourceData = resources.dataSource.filter(
        (resource) => resource.Id === data.DoctorId
      )[0];
      if (!resourceData) return;
      console.log(`resourceData`, resourceData);
      return resourceData.Color;
    },
    getHeaderTitle: function (data) {
      return "Appointment Details";
    },
    getHeaderDetails: function (data) {
      return (
        this.intl.formatDate(data.StartTime, {
          type: "date",
          skeleton: "full",
        }) +
        " (" +
        this.intl.formatDate(data.StartTime, { skeleton: "hm" }) +
        " - " +
        this.intl.formatDate(data.EndTime, { skeleton: "hm" }) +
        ")"
      );
    },
  },
});

var contentTemplateVue = Vue.component("contentTemplate", {
  template: `<div class="quick-info-content"><div class="e-cell-content" v-if="data.elementType === 'event'">
    <div class="content-area"><ejs-textbox ref="patientNameObj" id="patientName" placeholder="Patient name" v-model="data.Subject"></ejs-textbox></div>
    <div class="content-area"><ejs-dropdownlist ref="appointmentTypeObj" id="appointmentTypes" :dataSource="appointmentData" :index="0" :fields="fields" 
    popupHeight="200px" placeholder="Choose Appointment Type"></ejs-dropdownlist></div>
    <div class="content-area"><ejs-dropdownlist ref="providerObj" id="provider" :dataSource="providerData" v-model="data.DoctorId || 1" :fields="fields" 
    popupHeight="200px" placeholder="Choose Provider"></ejs-dropdownlist></div> <div class="content-area"><ejs-timepicker cssClass="time-selection"  id="timepicker-start" 
    placeholder="Start Time" :value="getTime(data, 'start')"></ejs-timepicker></div>
    <div class="content-area"><ejs-timepicker id="timepicker-end" placeholder="End Time" 
    :value="getTime(data, 'end')"></ejs-timepicker></div></div>
    </div>`,
  data() {
    return {
      fields: { text: "Name", value: "Id" },
      appointmentData: extend([], appointmentData, undefined, true),
      providerData: extend([], providerData, undefined, true),
      data: {},
    };
  },
  methods: {
    getTime(data, type) {
      return type === "start" ? data.StartTime : data.EndTime;
    },
    getPatientName(data) {
      console.log(`data`, data);
      const scheduleObj =
        document.querySelector(".e-schedule").ej2_instances[0];
      const resources = scheduleObj.getResourceCollections().slice(-1)[0];
      const resourceData = resources.dataSource.filter(
        (resource) => resource.Id === data.DoctorId
      )[0];
      console.log(`resourceData`, resourceData);
      if (!resourceData) return;
      return resourceData.Name;
    },
  },
});

var footerTemplateVue = Vue.component("footerTemplate", {
  template: `<div class="quick-info-footer"><div class="cell-footer" v-if="data.elementType === 'event'">
    <ejs-button id="more-details" cssClass="e-flat" :isPrimary="true" content="Join the video" v-on:click.native="$router.push('/app/video-call')"></ejs-button>
    <ejs-button id="more-details" cssClass="e-flat" content="More Details" v-on:click.native="buttonClickActions(data)"></ejs-button>
    <ejs-button id="save" cssClass="e-flat" :isPrimary="true" content="Save" v-on:click.native="saveDetails(data)"></ejs-button>
    </div></div>`,
  data: function () {
    return {
      data: {},
    };
  },
  methods: {
    saveDetails(data) {
      const scheduleObj =
        document.querySelector(".e-schedule").ej2_instances[0];
      const quickPopup = scheduleObj.element.querySelector(
        ".e-quick-popup-wrapper"
      );
      const patientName =
        quickPopup.querySelector("#patientName").ej2_instances[0].value;
      const provider =
        quickPopup.querySelector("#provider").ej2_instances[0].value;
      const timepickerStart =
        quickPopup.querySelector("#timepicker-start").ej2_instances[0].value;
      const timepickerEnd =
        quickPopup.querySelector("#timepicker-end").ej2_instances[0].value;
      const updatedData = {
        ...data,
        Subject: patientName,
        DoctorId: provider,
        StartTime: timepickerStart,
        EndTime: timepickerEnd,
      };
      scheduleObj.saveEvent(updatedData);
      scheduleObj.closeQuickInfoPopup();
    },
    buttonClickActions(data) {
      if (data.elementType === "event") {
        const element = document.querySelector(".patient-detail-sidebar");
        if (element) {
          element.classList.toggle("sidebar-open");
        }
        this.$root.$emit("bv::toggle::collapse", "sidebar-right");
      }

      // const scheduleObj = document.querySelector(".e-schedule")
      //   .ej2_instances[0];
      // const quickPopup = scheduleObj.element.querySelector(
      //   ".e-quick-popup-wrapper"
      // );
      // const getSlotData = function () {
      //   const titleObj = quickPopup.querySelector("#title").ej2_instances[0];
      //   const notesObj = quickPopup.querySelector("#notes").ej2_instances[0];
      //   const eventTypeObj = quickPopup.querySelector("#eventType")
      //     .ej2_instances[0];
      //   const cellDetails = scheduleObj.getCellDetails(
      //     scheduleObj.getSelectedElements()
      //   );
      //   let addObj = {};
      //   addObj.Id = scheduleObj.getEventMaxID();
      //   addObj.Subject = titleObj.value;
      //   addObj.StartTime = new Date(+cellDetails.startTime);
      //   addObj.EndTime = new Date(+cellDetails.endTime);
      //   addObj.Description = notesObj.value;
      //   addObj.RoomId = eventTypeObj.value;
      //   return addObj;
      // };
      // if (e.target.id === "add") {
      //   const addObj = getSlotData();
      //   scheduleObj.addEvent(addObj);
      // } else if (e.target.id === "delete") {
      //   const eventDetails = scheduleObj.activeEventData.event;
      //   let currentAction = "Delete";
      //   if (eventDetails.RecurrenceRule) {
      //     currentAction = "DeleteOccurrence";
      //   }
      //   scheduleObj.deleteEvent(eventDetails, currentAction);
      // } else {
      //   const isCellPopup = quickPopup.firstElementChild.classList.contains(
      //     "e-cell-popup"
      //   );
      //   const eventDetails = isCellPopup
      //     ? getSlotData()
      //     : scheduleObj.activeEventData.event;
      //   let currentAction = isCellPopup ? "Add" : "Save";
      //   if (eventDetails.RecurrenceRule) {
      //     currentAction = "EditOccurrence";
      //   }
      //   scheduleObj.openEditor(eventDetails, currentAction, true);
      // }
      // scheduleObj.closeQuickInfoPopup();
    },
  },
});

export default {
  components: { Loader },
  data() {
    return {
      resourceData: [],
      eventSettings: {
        dataSource: extend([], this.resourceData, null, true),
      },
      selectedDate: new Date(),
      group: { byDate: true, resources: ["Doctors"] },
      allowMultiple: true,
      showTimeIndicator: false,
      resourceDataSource: [
        {
          Text: "OP - 1",
          Id: 1,
          DoctorId: 1,
          Color: "#bbdc00",
          Designation: "Content writer",
        },
        {
          Text: "OP - 2",
          Id: 2,
          DoctorId: 2,
          Color: "#9e5fff",
          Designation: "Designer",
        },
        {
          Text: "OP - 3",
          Id: 3,
          DoctorId: 1,
          Color: "#bbdc00",
          Designation: "Software Engineer",
        },
        {
          Text: "OP - 4",
          Id: 4,
          DoctorId: 2,
          Color: "#9e5fff",
          Designation: "Support Engineer",
        },
        {
          Text: "Other Office",
          Id: 5,
          DoctorId: 1,
          Color: "#bbdc00",
          Designation: "Human Resource",
        },
      ],
      cssClas: "schedule-no-date",
      show: false,
      virtualScroll: true,
      currentView: "Day",
      calenderHieght: window.innerHeight - 200,
      fullscreen: false,
      quickInfoTemplates: {
        header() {
          return { template: headerTemplateVue };
        },
        content() {
          return { template: contentTemplateVue };
        },
        footer() {
          return { template: footerTemplateVue };
        },
      },
    };
  },
  computed: {
    ...mapGetters(["getPatientsList", "getLoading"]),
  },
  mounted() {
    this.setLoading(true);
    setTimeout(() => {
      this.setLoading(false);
    }, 2000);
    this.resourceData = this.getPatientsList;
    if (this.resourceData && this.resourceData.length) {
      const dataList = [];
      this.resourceData.forEach((d) => {
        dataList.push(this.createObject(d));
      });
      this.setResourceData(dataList);
    } else {
      this.setResourceData([]);
    }
  },
  methods: {
    ...mapActions([
      "setPatientData",
      "setActiveTabInPatientForm",
      "setLoading",
    ]),
    createObject(data) {
      return {
        Id: data.id,
        Subject: data.first_name + " " + data.last_name,
        StartTime: data.startTime,
        EndTime: data.endTime,
        IsAlive: data.onCall,
        DoctorId: data.doctorId,
      };
    },
    setResourceData(resourceData) {
      this.eventSettings.dataSource = resourceData;
      setTimeout(() => {
        this.show = true;
      }, 200);
    },
    onEventRendered: function (args) {
      let categoryColor = args.data.CategoryColor;
      if (args && args.data && args.data.IsAlive) {
        args.element.classList.add("live-event");
      }
      if (!args.element || !categoryColor) {
        return;
      }
      args.element.style.backgroundColor = categoryColor;
    },
    onActionBegin: function (args) {
      if (args.requestType === "toolbarItemRendering") {
        const fullScreenIconItem = {
          align: "Right",
          prefixIcon: "i-Full-Screen",
          cssClass: "full-screen-view-icon",
        };
        args.items.push(fullScreenIconItem);
        const dayNameElement = {
          align: "Left",
          prefixIcon: "",
          text: moment(this.selectedDate).format("dddd"),
          cssClass: "selected-day-name",
        };
        args.items.push(dayNameElement);
      }
    },
    onActionComplete: function (args) {
      let scheduleElement = document.getElementById("Schedule");
      if (args.requestType === "toolBarItemRendered") {
        let fullScreenIconItem = scheduleElement.querySelector(
          ".full-screen-view-icon"
        );
        fullScreenIconItem.onclick = () => {
          this.$fullscreen.toggle(this.$el.querySelector("#Schedule"), {
            wrap: false,
            callback: this.fullscreenChange,
          });
        };
      }
    },
    fullscreenChange(fullscreen) {
      this.fullscreen = fullscreen;
    },
    onNavigating(e) {
      this.selectedDate = e.currentDate;
      const element = document.querySelector(
        ".selected-day-name .e-tbar-btn-text"
      );
      if (element) {
        element.innerHTML = moment(this.selectedDate).format("dddd");
      }
      console.log(`e`, e);
    },
    onEventClick(e) {
      console.log(`this.resourceData`, this.resourceData);
      const { resourceData } = this;
      const { event } = e;
      const findResource = resourceData.find((d) => d.id === event.Id);
      let obj = null;
      if (findResource) {
        obj = findResource;
      } else {
        obj = {
          id: event.Id,
          name: event.Subject,
        };
      }
      this.setActiveTabInPatientForm("appt");
      this.setPatientData(obj);
      // const element = document.querySelector(".patient-detail-sidebar");
      // if (element) {
      //   element.classList.toggle("sidebar-open");
      // }
      // this.$root.$emit("bv::toggle::collapse", "sidebar-right");
    },
    onCellClick(e) {
      return;
    },
    onPopupOpen: (args) => {
      console.log(`args`, args);
      if (
        args &&
        args.target &&
        args.target.classList.contains("e-work-cells")
      ) {
        args.cancel = true;
      }
    },
  },
  provide: {
    schedule: [Day, Week, Month, Agenda, Resize, DragAndDrop],
  },
};
</script>