import Controller from '@ember/controller';
import { action } from "@ember/object";

export default class PreferencesController extends Controller {
  currentPass = "";
  newPass = "";
  newPassAgain = "";

  @action changePass() {
    const cp = this.currentPass;
    const np = this.newPass;
    const npa = this.newPassAgain;

    if (np !== npa) {
      this.set("message", "New passwords do not match");
      return;
    }
    this.set("message", "...");

    fetch("/api/update-pass", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        old: cp,
        new: np,
      }),
    }).then(r => r.json()).then(stuff => {
      if (stuff === "success") {
        this.set("message", "Updated successfully");
      } else {
        this.set("message", "Updating failed");
      }
    });


  }

}
