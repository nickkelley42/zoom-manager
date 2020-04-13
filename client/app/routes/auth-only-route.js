import Route from '@ember/routing/route';

export default class AuthOnlyRoute extends Route {
  beforeModel() {
    return fetch("/api/auth-test").then(r => r.json()).then(t => {
      if (t !== "Logged in") {
        this.transitionTo("login");
      }
    });
  }
}
