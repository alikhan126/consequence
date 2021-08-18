<template>
  <div class="main-content">
    <!-- <breadcumb :page="'Chat'" :folder="'apps'" /> -->

    <div class="card chat-sidebar-container sidebar-container">
      <div class="chat-content-wrap sidebar-content">
        <div
          class="d-flex pl-3 pr-3 pt-2 pb-2 o-hidden box-shadow-1 chat-topbar"
        >
          <a class="link-icon d-md-none" @click="isMobile = !isMobile">
            <i class="icon-regular i-Right ml-0 mr-3"></i>
          </a>
          <div class="d-flex align-items-center">
            <p class="m-0 text-title text-16 flex-grow-1">
              {{ getPatientData.first_name }} {{ getPatientData.last_name }}
            </p>
          </div>
        </div>
        <vue-perfect-scrollbar
          :settings="{ suppressScrollX: true, wheelPropagation: false }"
          class="chat-content perfect-scrollbar rtl-ps-none ps scroll"
        >
          <div>
            <div
              v-for="(chat, index) in getChats[0].chats"
              :key="chat.id"
              :class="`d-flex mb-30 ${index % 2 === 0 ? 'user' : ''}`"
            >
              <div class="message flex-grow-1 mr-5" v-if="index % 2 === 0">
                <div class="d-flex">
                  <p class="mb-1 text-title text-16 flex-grow-1">
                    {{ getSelectedUser.name }}
                  </p>
                  <span class="text-small text-muted">25 min ago</span>
                </div>
                <p class="m-0">
                  {{ chat.text }}
                </p>
              </div>
              <div
                :class="`message flex-grow-1 ml-5 ${
                  index % 2 !== 0 ? 'bg-blue' : ''
                }`"
                v-if="index % 2 !== 0"
              >
                <div class="d-flex">
                  <p class="mb-1 text-title text-16 flex-grow-1">Jhon Doe</p>
                  <span class="text-small text-muted">24 min ago</span>
                </div>
                <p class="m-0">Lorem ipsum dolor sit amet.</p>
              </div>
            </div>
          </div>
        </vue-perfect-scrollbar>

        <div class="pl-3 pr-3 pt-3 pb-3 box-shadow-1 chat-input-area">
          <form class="inputForm">
            <div class="form-group">
              <textarea
                class="form-control form-control-rounded"
                placeholder="Type your message"
                name="message"
                id="message"
                cols="30"
                rows="3"
                spellcheck="false"
              ></textarea>
            </div>
            <div class="d-flex">
              <div class="flex-grow-1"></div>
              <button class="btn btn-icon btn-rounded btn-primary mr-2">
                <i class="i-Paper-Plane"></i>
              </button>
              <button
                class="btn btn-icon btn-rounded btn-outline-primary"
                type="button"
              >
                <i class="i-Add-File"></i>
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import { mapGetters, mapActions } from "vuex";

export default {
  metaInfo: {
    // if no subcomponents specify a metaInfo.title, this title will be used
    title: "Chat",
  },
  data() {
    return {
      recentContacts: [],
      search: "",
      isMobile: false,
    };
  },
  methods: {
    ...mapActions(["changeSelectedUser"]),
    console() {
      console.log(this.test);
    },
  },

  computed: {
    ...mapGetters([
      "getContactLists",
      "getRecentUser",
      "getCurrentUser",
      "getSelectedUser",
      "getPatientData",
      "getChats",
    ]),
    filterContacts() {
      return this.getContactLists.filter((contact) => {
        return contact.name.toLowerCase().match(this.search.toLowerCase());
      });
    },
  },

  created: function () {
    console.log(this.getSelectedUser);
    // this.getCurrentUser.forEach(currentUser => {
    //   currentUser.chatInfo.forEach(user => {
    //     this.getContactLists.filter(contact => {
    //       if (user.contactId == contact.id) {
    //         this.recentContacts.push(contact);
    //       }
    //     });
    //   });
    // });
  },
};
</script>

<style>
.chat-sidebar-container {
  height: calc(100vh - 342px) !important;
  min-height: unset;
}
.chat-sidebar-container .chat-content-wrap .chat-content {
  height: calc(100vh - 532px) !important;
}
.chat-sidebar-container .chat-content-wrap {
  margin-left: 0 !important;
}
.chat-content .message.bg-blue {
  background: #24a0ed !important;
}
.chat-sidebar-container
  .chat-content-wrap
  .chat-content
  .message.bg-blue:before {
  background: #24a0ed !important;
  border-color: #24a0ed transparent #24a0ed transparent !important;
}
</style>

