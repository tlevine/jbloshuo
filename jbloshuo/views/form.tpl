% rebase('base.tpl', title = "Hire" + category_pretty)
<h1>Hire {{category_pretty}}</h1>
<form>
  <label name="name">What is your name?</label>
  <input name="name" type="text" />

  <label name="email">What is your email address?</label>
  <input name="email" type="email" />

  <label name="company">What is the company, if you are able to tell me?</label>
  <input name="company" type="text">

  <label name="description">Describe the {{description_noun}}</label>
  <textarea placeholder="Write about the {{description_noun}}, or provide a link to a description."
            name="description"></textarea>

  <label name="pay">{{pay_label}}</label>
  <select name="pay">
    % for option in pay_options:
    <option value="{{option}}">{{option}}</option>
    % end
  </select>

  % if category == 'employee':
  <label name="time">Is this position part-time or full-time?</label>
  <select name="time">
    <option value="part-time">Part-time</option>
    <option value="full-time">Full-time</option>
  </select>
  % end

  <label name="initiative">{{initiative_label}}</label>
  <input type="text" name="initiative" />

  <input type="submit" name="kind" value="{{category}}" />
</form>
