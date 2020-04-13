import Route from '@ember/routing/route';

export default class AuthOnlyRoute extends Route {
  beforeModel(transition) {
    return fetch("/api/auth-test").then(r => r.json()).then(t => {
      if (t !== "Logged in") {
        let loginController = this.controllerFor('login');
        loginController.set('previousTransition', transition);
        this.transitionTo("login");
      }
    });
  }
}
