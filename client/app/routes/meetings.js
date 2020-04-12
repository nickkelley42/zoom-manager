import Route from '@ember/routing/route';

export default class MeetingsRoute extends Route {
  beforeModel() {
    return fetch("/api/auth-test").then(r => r.text()).then(t => {
      if (t !== "Logged in") {
        this.transitionTo("login");
      }
    });
  }

  model() {
    return this.store.findAll("meeting");
  }
}
