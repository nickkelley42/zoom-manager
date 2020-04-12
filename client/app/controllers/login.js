import Controller from '@ember/controller';
import { action } from "@ember/object";

export default class LoginController extends Controller {
  username = "";
  password = "";

  @action login() {
    fetch("/api/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        username: this.username,
        password: this.password,
      }),
    }).then(response => {
      console.log(response.json());
    });
  }
}
