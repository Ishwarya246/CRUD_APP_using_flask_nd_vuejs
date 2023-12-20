import {createRouter , createWebHistory} from "vue-router"
import StudentDetails from "./pages/StudentDetails"


const routes = [
    {path : '/student-details' , component : StudentDetails}
] 

const router = createRouter({
    history : createWebHistory(),
    routes,
})

export default router ;