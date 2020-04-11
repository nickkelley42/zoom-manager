import Route from '@ember/routing/route';

export default class MeetingsRoute extends Route {
  model() {
    return this.store.findAll("meeting")
      .catch(() => {
        this.transitionTo("login");
      });
  }
}
