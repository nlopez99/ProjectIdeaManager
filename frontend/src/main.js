import Vue from "vue";
import App from "./App.vue";
import router from "./routes/index";
import * as firebase from "firebase";
import store from "./store";

Vue.config.productionTip = false;

const configOptions = {
  apiKey: "AIzaSyApJcKyP46biQ9Sn1tti0xQUOf0Al34Kj0",
  authDomain: "projectmanager-41da6.firebaseapp.com",
  databaseURL: "https://projectmanager-41da6.firebaseio.com",
  projectId: "projectmanager-41da6",
  storageBucket: "projectmanager-41da6.appspot.com",
  messagingSenderId: "77268525587",
  appId: "1:77268525587:web:4691d969a29b1cdf6555e6",
  measurementId: "G-8P5SEKNWKS"
};

firebase.initializeApp(configOptions);

firebase.auth().onAuthStateChanged(user => {
  store.dispatch("fetchUser", user);
});

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");