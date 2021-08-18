<template>
  <div class="main-content">
    <b-row>
      <b-col lg="12" xl="12" md="12">
        <div class="d-flex justify-content-between">
          <div class="d-flex align-items-center mb-4">
            <div class="mr-3 page-title">
              <h3 class="font-weight-bold m-0">Users</h3>
            </div>
          </div>
        </div>
      </b-col>
      <b-col md="12">
        <b-card no-body>
          <b-card-header class="gradient-purple-indigo o-hidden pb-80">
            <div class="pt-4">
              <b-row>
                <h4 class="col-md-4 text-white">Users</h4>
                <b-form-input
                  type="text"
                  class="form-control-rounded col-md-4 ml-3 mr-3"
                  placeholder="Search"
                ></b-form-input>
              </b-row>
            </div>
          </b-card-header>
          <b-card-body>
            <div class="ul-contact-list-body">
              <div class="ul-contact-main-content d-flex">
                <div
                  class="ul-contact-left-side"
                  :class="{ 'contact-list-mobile': isCLoseMenu }"
                >
                  <b-card class="ul-contact-vh">
                    <div class="contact-close-mobile-icon float-right mb-2">
                      <i
                        @click="isCLoseMenu = !isCLoseMenu"
                        class="i-Close-Window text-15 font-weight-600"
                      ></i>
                    </div>
                    <div class="ul-contact-list">
                      <b-button
                        variant="outline-secondary"
                        class="mb-30"
                        block
                        @click="onContactListBtn"
                        v-b-modal.contact-list-table-modal
                        >ADD USER</b-button
                      >
                      <b-modal
                        id="contact-list-table-modal"
                        centered
                        title="User Details"
                        hide-footer
                        ref="my-modal"
                      >
                        <b-form @submit="onContactListSubmit" @reset="onReset">
                          <b-form-group id="input-group-1" label-for="input-1">
                            <b-form-input
                              id="input-1"
                              v-model="userListForm.name"
                              type="text"
                              required
                              placeholder="Enter your name"
                            ></b-form-input>
                          </b-form-group>
                          <b-form-group id="input-group-1" label-for="input-1">
                            <b-form-input
                              id="input-1"
                              v-model="userListForm.email"
                              type="email"
                              required
                              placeholder="Enter email"
                            ></b-form-input>
                          </b-form-group>

                          <b-form-group id="input-group-2" label-for="input-2">
                            <b-form-input
                              id="input-2"
                              type="text"
                              v-model="userListForm.phone"
                              required
                              placeholder="Phone number"
                            ></b-form-input>
                          </b-form-group>
                          <b-form-group>
                            <b-button
                              v-if="isSaveBtn"
                              type="submit"
                              variant="success"
                              >Submit</b-button
                            >
                            <b-button
                              v-else-if="isUpdateBtn"
                              type="submit"
                              variant="success"
                              >Update</b-button
                            >
                          </b-form-group>
                        </b-form>
                      </b-modal>
                      <b-list-group flush>
                        <b-list-group-item
                          button
                          class="
                            d-flex
                            justify-content-between
                            align-items-center
                          "
                          >Cras justo odio</b-list-group-item
                        >

                        <b-list-group-item
                          button
                          class="
                            d-flex
                            justify-content-between
                            align-items-center
                          "
                          >Dapibus ac facilisis in</b-list-group-item
                        >

                        <b-list-group-item
                          button
                          class="
                            d-flex
                            justify-content-between
                            align-items-center
                          "
                          >Morbi leo risus</b-list-group-item
                        >
                      </b-list-group>
                    </div>
                  </b-card>
                </div>

                <div class="ul-contact-content">
                  <b-card>
                    <div class="navbar-header clearfix">
                      <i
                        @click="openMenu"
                        class="
                          nav-icon
                          i-Align-Justify-All
                          text-25
                          ul-contact-mobile-icon
                          float-left
                        "
                      ></i>
                    </div>
                    <vue-good-table
                      :line-numbers="false"
                      :columns="columns"
                      :pagination-options="{
                        enabled: true,
                        mode: 'records',
                      }"
                      styleClass="tableOne vgt-table"
                      :rows="rows"
                    >
                      <template slot="table-row" slot-scope="props">
                        <span v-if="props.column.field == 'action'">
                          <b-dropdown
                            id="dropdown-left"
                            variant="link"
                            text="Left align"
                            toggle-class="text-decoration-none"
                            size="sm"
                            dropleft
                            no-caret
                          >
                            <template
                              v-slot:button-content
                              class="_r_btn border-0"
                            >
                              <span class="_dot _r_block-dot"></span>
                              <span class="_dot _r_block-dot"></span>
                              <span class="_dot _r_block-dot"></span>
                            </template>
                            <b-dropdown-item
                              v-b-modal.contact-list-table-modal-2
                              @click="editContactlist(props.row)"
                            >
                              
                              
                            </b-dropdown-item>

                            <b-dropdown-item
                              @click="deleteContactList(props.index)"
                            >
                              <i
                                class="
                                  nav-icon
                                  i-Close-Window
                                  text-danger
                                  font-weight-bold
                                  mr-2
                                "
                              ></i>
                              Delete
                            </b-dropdown-item>
                          </b-dropdown>
                        </span>
                      </template>
                    </vue-good-table>
                  </b-card>

                  <!-- edit-modal  -->
                  <div class="edit-modal">
                    <b-modal
                      id="contact-list-table-modal-2"
                      centered
                      :title="editUserListForm.name"
                      hide-footer
                    >
                      <b-form @submit.stop.prevent="onUpdateUserList">
                        <b-form-group id="input-group-1" label-for="input-1">
                          <b-form-input
                            id="input-1"
                            v-model="editUserListForm.name"
                            type="text"
                            required
                            placeholder="Enter your name"
                          ></b-form-input>
                        </b-form-group>
                        <b-form-group id="input-group-1" label-for="input-1">
                          <b-form-input
                            id="input-1"
                            v-model="editUserListForm.email"
                            type="email"
                            required
                            placeholder="Enter email"
                          ></b-form-input>
                        </b-form-group>

                        <b-form-group id="input-group-2" label-for="input-2">
                          <b-form-input
                            id="input-2"
                            type="text"
                            v-model="editUserListForm.phone"
                            required
                            placeholder="Phone number"
                          ></b-form-input>
                        </b-form-group>
                        <b-form-group>
                          <b-button
                            type="submit"
                            variant="success"
                            @click="onUpdateUserList"
                            >Update</b-button
                          >
                        </b-form-group>
                      </b-form>
                    </b-modal>
                  </div>
                </div>
              </div>
            </div>
          </b-card-body>
        </b-card>
      </b-col>
    </b-row>
  </div>
</template>
<script>
export default {
  data() {
    return {
      isCLoseMenu: true,
      show: true,
      isSaveBtn: true,
      isUpdateBtn: false,
      editUserListForm: [],
      userListFilter: "",
      userListForm: [
        {
          id: "",
          name: "",
          email: "",
          phone: "",
        },
      ],
      columns: [
        {
          label: "Id",
          field: "id",
        },
        {
          label: "Name",
          field: "name",
          html: true,
        },
        {
          label: "Email",
          field: "email",
        },
        {
          label: "Phone",
          field: "phone",
          type: "number",
        },
        {
          label: "Action",
          field: "action",
        },
      ],
      rows: [
        {
          id: 1,
          name: "Wireless Bluetooth V4.0 Portable Speaker with HD Sound and Bass",
          email: "green.kip@schuster.com",
          phone: 0.03343,
        },
        {
          id: 2,
          name: "Portable Speaker with HD Sound",
          email: "lempi93@hotmail.com",
          phone: 0.03343,
        },
        {
          id: 3,
          name: "Lightweight On-Ear Headphones - Black",
          email: "roxanne15@yahoo.com",
          phone: 0.03343,
        },
        {
          id: 4,
          name: "Automatic-self-wind mens Watch 5102PR-001 (Certified Pre-owned)",
          email: "holly92@hotmail.com",
          phone: 0.03343,
        },
        {
          id: 5,
          name: "Automatic-self-wind mens Watch 5102PR-001",
          email: "witting.guido@yahoo.com",
          phone: 0.03343,
        },
        {
          id: 6,
          name: "On-Ear Headphones - Black",
          email: "lilliana.kilback@veum.com",
          phone: 0.03343,
        },
        {
          id: 7,
          name: "In-Ear Headphone",
          email: "alyce60@dooley.com",
          phone: 0.03343,
        },
        {
          id: 8,
          name: "Duis exercitation nostrud anim",
          email: "gparisian@hotmail.com",
          phone: 0.03343,
        },
        {
          id: 9,
          name: "Doasdlor eu nostrud excepteur",
          email: "ritchie.beau@hotmail.com",
          phone: 0.03343,
        },
        {
          id: 10,
          name: "Over-Ear Headphones, Stereo Lightweight Adjustable Wired Headset",
          email: "ritchie.beau@hotmail.com",
          phone: 0.03343,
        },
        {
          id: 11,
          name: "Wireless Bluetooth V4.0 Portable Speaker with HD Sound and Bass",
          email: "zkunze@gmail.com",
          phone: 0.03343,
        },
        {
          id: 12,
          name: "Portable Speaker with HD Sound",
          email: "gparisian@hotmail.com",
          phone: 0.03343,
        },
      ],
    };
  },
  computed: {
    filterIcons() {
      return this.rows.filter((iconSearch) => {
        return this.userListFilter
          .toLowerCase()
          .match(this.search.toLowerCase());
      });
    },
  },
  methods: {
    openMenu() {
      this.isCLoseMenu = !this.isCLoseMenu;
    },
    onContactListBtn() {
      this.isUpdateBtn = false;
      this.isSaveBtn = true;
    },
    onContactListSubmit(evt) {
      evt.preventDefault();

      this.rows.push({
        id: this.rows.length + 1,
        name: this.userListForm.name,
        email: this.userListForm.email,
        phone: this.userListForm.phone,
      });
      this.onReset();
      this.$swal({
        toast: true,
        position: "top-end",
        showConfirmButton: false,
        timer: 3000,
        type: "success",
        title: "Data Inserted Successfully",
      });
    },

    onReset(evt) {
      (this.userListForm.name = ""),
        (this.userListForm.email = ""),
        (this.userListForm.phone = "");
    },
    editContactlist(data) {
      this.isUpdateBtn = true;
      this.isSaveBtn = false;
      this.editUserListForm = data;
    },
    onUpdateUserList(evt) {
      evt.preventDefault();
      let modifiedList = this.rows.map((row) => {
        // console.log(row.id, this.editUserListForm.id);

        this.$refs["my-modal"].hide();
        this.$swal({
          position: "top-end",
          type: "warning",
          title: "Your work has been saved",
          showConfirmButton: false,
          timer: 1000,
        });

        if (row.id == this.editUserListForm.id) {
          return this.editUserListForm;
        } else {
          return row;
        }
      });
      this.rows = modifiedList;
    },

    deleteContactList(data) {
      // console.log(data);

      this.$swal({
        title: "Are you sure?",
        text: "You won't be able to revert this!",
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Yes, delete it!",
      }).then((result) => {
        if (result.value) {
          this.$delete(this.rows, data);
          this.$swal("Deleted!", "Your file has been deleted.", "success");
        }
      });
    },
  },
};
</script>
<style scoped>
.gradient-purple-indigo {
  /* background-color: #a855f7; */
  background-image: -o-linear-gradient(-154deg, #a855f7 0%, #33214b 100%);
  background: linear-gradient(104deg, #00ced7 0%, #33214b 100%);
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='$from', endColorstr='$to',GradientType=1 );
}
</style>