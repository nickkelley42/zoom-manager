import Controller from '@ember/controller';
import $ from "jQuery";

export default class LoginController extends Controller {
  username = "";
  password = "";

  actions = {
    login() {
      $.post("/api/login", {
        username: this.username,
        password: this.password,
      });
    }
  };
}
