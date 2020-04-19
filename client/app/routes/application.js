import Route from '@ember/routing/route';
import { action } from '@ember/object';

export default class ApplicationRoute extends Route {
  @action error(error, transition) {
    if (Array.isArray(error.errors) && error.errors[0].status === '403') {
      let loginCtl = this.controllerFor('login');
      loginCtl.previousTransition = transition;
      this.transitionTo('login');
    } else {
      return true;
    }
  }
}
