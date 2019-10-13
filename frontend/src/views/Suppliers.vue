<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Suppliers</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.supplier-modal>Add Supplier</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Author</th>
              <th scope="col">Read?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(supplier, index) in suppliers" :key="index">
              <td>{{ supplier.name }}</td>
              <td>{{ supplier._created }}</td>
              <td>
                <span v-if="supplier._updated">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">Edit</button>
                  <button type="button" class="btn btn-danger btn-sm" @click="onDeleteSupplier(supplier)">Delete</button>
                  <button type="button" class="btn btn-primary btn-sm">Create Order</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addSupplierModal"
             id="supplier-modal"
             title="Add a new supplier"
             hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-title-group"
                    label="Title:"
                    label-for="form-title-input">
          <b-form-input id="form-name-input"
                        type="text"
                        v-model="addSupplierForm.name"
                        required
                        placeholder="Enter name">
          </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return {
            suppliers: [],
             addSupplierForm: {
                name: ''
             }
          };
    },
    methods: {
        getSuppliers() {
            const path = 'http://localhost:5000/supplier';
            axios.get(path)
                .then((res) => {
                   // eslint-disable-next-line
                    console.log(res.data);
                    this.suppliers = res.data._items;
                })
                .catch((error) => {
                   // eslint-disable-next-line
                    console.error(error);
                });
        },
        addSupplier(payload) {
          const path = 'http://localhost:5000/supplier';
          axios.post(path, payload)
            .then(() => {
              this.getSuppliers();
            })
            .catch((error) => {
              // eslint-disable-next-line
              console.log(error);
              this.getSuppliers();
            });
        },
        removeSupplier(supplierID,etag) {
          const path = `http://localhost:5000/supplier/${supplierID}`;
            let config = {
              headers: {
                "If-match": etag,
              }
            }
          axios.delete(path,config)
            .then(() => {
              this.getSuppliers();
              this.message = 'Supplier removed!';
              this.showMessage = true;
            })
            .catch((error) => {
              // eslint-disable-next-line
              console.error(error);
              this.getSuppliers();
            });
        },
        onDeleteSupplier(supplier) {
          this.removeSupplier(supplier._id,supplier._etag);
        },
        initForm() {
          this.addSupplierForm.name = '';
        },
        onSubmit(evt) {
          evt.preventDefault();
          this.$refs.addSupplierModal.hide();
          const payload = {
            name: this.addSupplierForm.name,
          };
          this.addSupplier(payload);
          this.initForm();
        },
        onReset(evt) {
          evt.preventDefault();
          this.$refs.addSupplierModal.hide();
          this.initForm();
        },
      },
    created() {
        this.getSuppliers();
    },
};
</script>
