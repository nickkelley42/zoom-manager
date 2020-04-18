import Controller from '@ember/controller';
import { action } from '@ember/object';

export default class MeetingsNewController extends Controller {
  @action submit() {
    let meeting = this.get('model');
    this.set('message', '...');
    this.set('sending', true);
    meeting.save().then(() => {
      this.set('sending', false);
      this.set('message', '');
      this.transitionToRoute('meetings.index');
    });
  }
}
