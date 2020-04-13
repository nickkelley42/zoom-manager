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
    }).then(response => response.text()).then(text => {
      if (text === "success") {
        this.set("message", null);
        let pt = this.get("previousTransition");
        this.set("previousTransition", null);
        pt.retry();
      } else {
        this.set("message", "Incorrect username/password");
      }
    });
  }
}
