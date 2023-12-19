<template>

  <div class="f21"> 
    <article class="f22" style="width: 60%;">
      <h1 class="f11">Student List</h1>

      <div class="f44"><div class="f55" style="width:27% ">NAME </div> <div class="f55" style="width:4%" >AGE</div><div class="f55" style="width:40%" >EMAIL</div> <div class="f55" style="width:10%">GENDER</div> <div class="f55" style="width:15%">Options</div>
      </div>

      <div class="f44" v-for="stud in list" :key="stud"><div class="f55" style="width:27%">{{ stud.name }}</div> <div class="f55" style="width:4%" >{{ stud.age }}</div><div class="f55" style="width:40%" >{{ stud.email }}</div> <div class="f55" style="width:10%">{{ stud.gender }}</div> <div class="f55" style="width:15%"><button class="f66"> Edit</button> <button class="f66"> Delete</button></div>
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

        <label class="label" >Gender </label>
        <input class="input" type = "text" v-model.trim ="gender"  value="" placeholder="Your Gender" required/>
        <br>

        <div class="f33">
          <button class="button" type="submit" > Save </button>
        </div>
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

.f66{
  color: blue;
  font-family: cursive;
  font-size: 100%;
  font-weight : bold;
  /* border-color: black; */
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