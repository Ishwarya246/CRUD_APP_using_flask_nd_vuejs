<template>
  <AppHeader />
  <StudentDetails />
  <router-view></router-view>
</template>

<script>
import AppHeader from './components/AppHeader.vue'
import StudentDetails from './pages/StudentDetails.vue'
export default {
  components: { AppHeader, StudentDetails},
}
</script>

<style>

</style>