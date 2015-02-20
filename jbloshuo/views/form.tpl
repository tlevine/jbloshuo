% rebase('base.tpl', title = "Hire " + category_pretty)
<h1>Hire {{category_pretty}}</h1>
<form>
  <label name="name">What is your <strong>name</strong>?</label>
  <input name="name" type="text" />

  <label name="email">What is your <strong>email address</strong>?</label>
  <input name="email" type="email" />

  <label name="company">What is the <strong>company</strong>, if you are able to tell me?</label>
  <input name="company" type="text">

  <label name="description">Describe the {{description_noun}}.</label>
  <textarea placeholder="Write about the {{description_noun}}, or provide a link to a description."
            name="description"></textarea>

  <label name="pay">{{!pay_label}}</label>
  <select name="pay">
    % for option in pay_options:
    <option value="{{option}}">{{option}}</option>
    % end
  </select>

  % if category == 'employee':
  <label name="time">Is this position <strong>part-time or full-time</strong>?</label>
  <select name="time">
    <option value="part-time">Part-time</option>
    <option value="full-time">Full-time</option>
  </select>
  % end

  <label name="initiative">{{initiative_label}}</label>
  <textarea name="initiative" placeholder="{{initiative_placeholder}}" /></textarea>

  <input type="hidden" name="kind" value="{{category}}" />

  <input type="submit" name="kind" value="Submit" />
</form>
