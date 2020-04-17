import Model, { attr } from '@ember-data/model';

export default class MeetingModel extends Model {
  @attr('string') topic;
  @attr('date')  start_time;
  @attr('string') join_url;
  @attr('number') duration;
}
