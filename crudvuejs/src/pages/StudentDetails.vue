<template>

  <div class="f21"> 
    <article class="f22" style="width: 60%;">
      <h1 class="f11">Student List</h1>

      <div class="f44"> <div class="f55" style="width:10%">ROLL NO</div>  <div class="f55" style="width:27% ">NAME </div> <div class="f55" style="width:4%" >AGE</div><div class="f55" style="width:40%" >EMAIL</div> <div class="f55" style="width:15%">OPTIONS</div>
      </div>

      <div class="f44" v-for="(stud,i) in list" :key="i"><div class="f55" style="width:10%">{{ stud.rollno }}</div> <div class="f55" style="width:27%">{{ stud.name }}</div> <div class="f55" style="width:4%" >{{ stud.age }}</div><div class="f55" style="width:40%" >{{ stud.email }}</div>  <div class="f55" style="width:15%"><button class="f66" @click="edit(i)"> Edit</button> <button class="f66" @click="remove(i)"> Delete</button></div>
      </div>

    </article>

    <article class="f22" style="width: 30%;">
      <h1 class="f11">Create new entry</h1>


      <form @submit.prevent="addDetails">
        <label class="label">Name </label> 
        <input class="input" value=""  type = "text" v-model.trim ="name" placeholder="Your Name" required/>
        <br>

        <label class="label" >Age </label>
        <input class="input" type = "text" v-model.trim ="age" value="" placeholder="Your Age" required/>
        <br>

        <label class="label" >Email </label>
        <input class="input" type = "email" v-model.trim ="email" value="" placeholder="Your Email" required/>
        <br>

        <label class="label" >rollno </label>
        <input class="input" type = "text" v-model.trim ="rollno"  value="" placeholder="Your rollno" required/>
        <br>

        <div class="f33">
          <button class="button" type="submit" > Save </button>
        </div>
      </form>
    </article>


    <article class="f22" v-if="isEdit">
      <h1 class="f11">Update Student details</h1>


      <form @submit.prevent="updateDetails">
        <label class="label">Name </label> 
        <input class="input" value=""  type = "text" v-model.trim ="editname" placeholder="Your Name" required/>
        <br>

        <label class="label" >Age </label>
        <input class="input" type = "text" v-model.trim ="editage" value="age" placeholder="Your Age" required/>
        <br>

        <label class="label" >Email </label>
        <input class="input" type = "email" v-model.trim ="editemail" value="email" placeholder="Your Email" required/>
        <br>

        <label class="label" >rollno </label>
        <input class="input" type = "text" v-model.trim ="editrollno"  value="rollno" placeholder="Your rollno" disabled="true" />
        <br>

        <div class="f33">
          <button class="button" type="submit" > Update </button>
        </div>
      </form>
    </article>

  </div>
</template>

<script>

import axios from 'axios';

export default {

  data(){
    return{
      list : [],
      name : "",
      age : "",
      email : "",
      rollno : "",
      iter : "",
      isEdit : false,
      editname : "",
      editage : "",
      editemail : "",
      editrollno : "",
      ind : "",
      res : ""
    }
  },
  methods : {

    getDetails(){
      const path = 'http://localhost:5000/select';
      axios.get(path)
      .then(response => {
        this.list = response.data
      })
      .catch(err => {
        console.log(err)
      })
    },
    addDetails(){
      this.getDetails();
      const path = 'http://localhost:5000/insert';
      axios.post(path, {
        name : this.name,
        email : this.email,
        age : this.age,
        rollno : this.rollno
      })
      .then(response => {
        console.log(response);
      })
      .catch(err =>{
        console.log(err);
      });
      this.getDetails();
      
      this.name = "",
      this.age = "",
      this.email = "",
      this.rollno = ""
    },
    
    edit(i){
      this.ind = i,
      this.isEdit = true,
      this.editname = this.list[i].name,
      this.editage = this.list[i].age,
      this.editemail = this.list[i].email,
      this.editrollno = this.list[i].rollno
    },

    remove(index){
      this.getDetails();
      const path = 'http://localhost:5000/delete';
      axios.put(path , {rollno : this.list[index].rollno})
      .then (response => {
        console.log(response)
      })
      .catch(err => {
        console.log(err)
      } )
      this.getDetails();
    },

    updateDetails(){
      this.getDetails();
      const path = 'http://localhost:5000/update';
      axios.put(path , {
        name : this.editname,
        email : this.editemail,
        age : this.editage,
        rollno : this.editrollno
      })
      .then(response => {
        console.log(response)
      })
      .catch(err => {
        console.log(err)
      })
      // this.getDetails();
      // this.list[this.ind].name = this.editname,
      // this.list[this.ind].email = this.editemail,
      // this.list[this.ind].age = this.editage,
      // this.list[this.ind].rollno = this.editrollno,
      this.getDetails();
      this.ind = "",
      this.isEdit = false,
      this.editname = "",
      this.editage = "",
      this.editemail = "",
      this.editrollno = ""
    }
  }
}

</script>

<style>

.f66{
  color: blue;
  font-family: cursive;
  font-size: 100%;
  font-weight : bold;
  border-radius: 10px;
  background-color: hsl(34, 40%, 90%);
}

.f55{
  background-color: hsl(34, 40%, 90%);
  width: 20%;
  color: blue;
  font-family: cursive;
  font-size: 100%;
  padding: 2.5px;
  border-color: black;
  margin: 1px;
  font-weight : bold;
}

.f44{
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  background-color: hsl(33, 76%, 71%);
  padding: 5px;
  margin: 2px;
  height: 1cm;
}

.f33{
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  margin: 5%;
}

.button{
  /* display: inline; */
  color :blue;
  font-family: cursive;
  font-size: 20px;
  background-color: antiquewhite;
}
.label{
  font-family: cursive;
  font-size: 20px;
  padding: 2px;
  
}

.input{
  font-size:20px ;
  width: 70%;
  height: 50;
  margin: 2px;
  padding: 2px;
  color:blue;
  font-family: cursive;
  
}

.f21{
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  justify-content: center;
}

.f22{
  /* display: flex; */
  margin: 5px;
  background-color: rgb(215, 255, 245);
  padding: 2px;
  /* flex-wrap: wrap; */
  justify-content: center;
  width: 45%;
  /* flex-direction: column; */
}

.f11{
  text-align: center;
  font-family: cursive;
  color :brown
}

</style>