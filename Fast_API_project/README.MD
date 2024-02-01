Pizza Delivery APIs.
Routes to implement

Method		route					            functionality				Access.
----------------------------------------------------------------------------------------------------------
POST		/api/signup/			       	    Regitser new user			All user
POST		/api/login/				            login user				    All user
POST		/api/order/				            place an order				all user
PUT		    /api/order/update/{order_id}/		Update an order				All user
PUT		    /api/order/status/{order_id}/		Update order on status		super user
DELETE		/api/order/delete/{order_id}		Delete/Remove an order		all user
GET		    /api/user/orders/			        Get users orders            All user
GET		    /api/orders/				        list all orders made	    All user
GET		    /api/orders/{order_id}			    Retrive an order            super user
GET		    /api/user/order/{order_id}		    Get user specific order         
GET         /docs/                              View Api Documentations    super user