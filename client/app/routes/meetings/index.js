import Route from '@ember/routing/route';

export default class MeetingsIndexRoute extends Route {
  model() {
    return this.store.findAll("meeting");
  }
}
