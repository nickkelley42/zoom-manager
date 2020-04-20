import Route from '@ember/routing/route';
import { action } from '@ember/object';

export default class MeetingsNewRoute extends Route {
  model() {
    return this.store.createRecord('meeting');
  }

  @action willTransition() {
    let model = this.controller.model;
    if (model.isNew) {
      model.unloadRecord();
    }
    return true;
  }
}
