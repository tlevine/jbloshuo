% rebase('base.tpl', title = "Hire " + category_pretty)
<h1>Hire {{category_pretty}}</h1>
% if error_message:
<p class="error">{{error_message}}</p>
% end
<form method="post" action="submit">
  <label name="name">What is your <strong>name</strong>?</label>
  <input name="name" type="text" value="{{name_value}}" />

  <label name="email">What is your <strong>email address</strong>?</label>
  <input name="email" type="email" value="{{email_value}}" />

  <label name="company">What is the <strong>company</strong>, if you are able to tell me?</label>
  <input name="company" type="text" value="{{company_value}}" />

  <label name="description">Describe the {{description_noun}}.</label>
  <textarea placeholder="Write about the {{description_noun}}, or provide a link to a description."
            name="description">{{description_value}}</textarea>

  <label name="pay">{{!pay_label}}</label>
  <select name="pay">
    <option value="empty">Choose the closest one.</option>
    % for option in pay_options:
    <option value="{{option}}">{{option}}</option>
    % end
  </select>

  % if category == 'employee':
  <label name="time">Is this position <strong>part-time or full-time</strong>?</label>
  <select name="time">
    <option value="empty"></option>
    <option value="part-time">Part-time</option>
    <option value="full-time">Full-time</option>
  </select>
  % end

  <label name="initiative">{{initiative_label}}</label>
  <textarea name="initiative" placeholder="{{initiative_placeholder}}" />{{initiative_value}}</textarea>

  <input type="hidden" name="category" value="{{category}}" />

  <input type="submit" name="submit" value="Submit" />
</form>
