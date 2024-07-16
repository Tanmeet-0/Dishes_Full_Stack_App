import { useState} from "react";
import { URL } from "./index.js";

function get_json_data(set_data) {
  fetch(URL + "dishes/").then(
    (good_response) => {
      good_response.json().then((json_data) => set_data(json_data));
    },
    (bad_response) => {
      console.log(bad_response);
    }
  );
}

export default function Dashboard() {
  const [dishes, set_dishes] = useState([]);
  const [is_timer_on, set_is_timer_on] = useState(false);
  if(!is_timer_on){
    setInterval(() => get_json_data(set_dishes),100);
    set_is_timer_on(true);
  }
  return (
    <div className="dashboard">
      <Header />
      <Dishes dishes={dishes} />
    </div>
  );
}

function Header() {
  return <div className="header">Dishes Dashboard</div>;
}

function Dishes({ dishes }) {
  function handle_toggle_publish(dish){
    fetch(URL + "dishes/toggle_publish/"+dish.dishId+"/").catch(error => console.log(error));
  }
  return (
    <div className="dishes">
      {dishes.map((dish) => (
        <Dish key={dish.dishId} dish={dish} handle_toggle_publish={handle_toggle_publish}/>
      ))}
    </div>
  );
}
function Dish({ dish ,handle_toggle_publish}) {
  return (
    <div className="dish">
      <img className="dish_image" src={dish.imageUrl} alt={dish.dishName} />
      <div className="dish_name">{dish.dishName}</div>
      <div className="dish_published">
        Published
        <label className="switch">
          <input
            type="checkbox"
            className="dish_published_checkbox"
            checked={dish.isPublished}
            onChange={() => handle_toggle_publish(dish)}
          />
          <span className="slider round"></span>
        </label>
      </div>
    </div>
  );
}
