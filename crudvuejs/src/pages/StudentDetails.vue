<template>

  <div class="f21"> 
    <article class="f22">
      <h1 class="f11">Student List</h1>

      <p>
        <ul>
          <li v-for="stud in list" :key="stud">{{ stud.name }} {{ stud.age }} {{ stud.email }} {{ stud.gender }} </li>
        </ul>
      </p>
    </article>

    <article class="f22">
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

        <label class="label" >Gender </label>
        <input class="input" type = "text" v-model.trim ="gender"  value="" placeholder="Your Gender" required/>
        <br>

        <!-- <div class="f33"> -->
          <button class="button" type="submit" > Save </button>
        <!-- </div> -->
      </form>
    </article>
  </div>

</template>

<script>
export default {

  data(){
    return{
      list : [],
      name : "",
      age : "",
      email : "",
      gender : ""
    }
  },
  methods : {
    save(){
      return "Hello"
    },
    addDetails(){
      this.list.push ({"name" : this.name , "email" : this.email , "age" : this.age , "gender":this.gender}),
      this.name = "",
      this.age = "",
      this.email = "",
      this.gender = ""
    }
  }
}
</script>

<style>

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