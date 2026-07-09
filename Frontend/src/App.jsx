import { useEffect, useState } from "react"
import "./App.css"
import "./index.css"


function App() {

    const [inventory, setInventory] = useState([])

    const [formData, setFormData] = useState({
    name: "",
    quantity: "",
    price: ""
})

    async function fetchInventory() {

        try {

            const response = await fetch(
                "https://python-rest-api-1.onrender.com/items"
            )

            const data = await response.json()

            setInventory(data)

        } catch (error) {

            console.log(
                "Error fetching inventory:",
                error
            )
        }
    }

    useEffect(() => {

        fetchInventory()

    }, [])

    function handleChange(event) {

        setFormData({

            ...formData,

            [event.target.name]:
                event.target.value
        })
    }

    async function addItem(event) {

        event.preventDefault()

        try {

            const response = await fetch(

            "https://python-rest-api-1.onrender.com/items",

                {

                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({

                        ...formData,

                        quantity:
                            Number(formData.quantity),

                        price:
                            Number(formData.price)
                    })
                }
            )

            if (response.ok) {

                fetchInventory()

                setFormData({

                    name: "",
                    quantity: "",
                    price: ""
                })
            }

        } catch (error) {

            console.log(
                "Error adding item:",
                error
            )
        }
    }

    async function deleteItem(id) {

        try {

            await fetch(

                `https://python-rest-api-1.onrender.com/items/${id}`,

                {
                    method: "DELETE"
                }
            )

            fetchInventory()

        } catch (error) {

            console.log(
                "Error deleting item:",
                error
            )
        }
    }

    return (

        <div style={{ padding: "20px" }}>

            <h1>
                Inventory Management System
            </h1>

            <form onSubmit={addItem}>

                <input
                    type="text"
                    name="name"
                    placeholder="Product Name"
                    value={formData.name}
                    onChange={handleChange}
                />

                <br /><br />

                <input
                    type="number"
                    name="quantity"
                    placeholder="Quantity"
                    value={formData.quantity}
                    onChange={handleChange}
                />

                <br /><br />

                <input
                    type="number"
                    step="0.01"
                    name="price"
                    placeholder="Price"
                    value={formData.price}
                    onChange={handleChange}
                />

                <br /><br />

                <button type="submit">
                    Add Item
                </button>

            </form>

            <hr />

            <h2>Inventory</h2>

            {inventory.length === 0 ? (

                <p>No inventory items found.</p>

            ) : (

                inventory.map((item) => (

                    <div
                        key={item.id}
                        style={{
                            border: "1px solid black",
                            padding: "10px",
                            marginBottom: "10px"
                        }}
                    >

                        <p>
                            <strong>Name: </strong>{item.name}
                        </p>

                        <p>
                            Quantity: {item.quantity}
                        </p>

                        <p>
                            Price: ${item.price}
                        </p>

                        <button
                            onClick={() =>
                                deleteItem(item.id)
                            }
                        >
                            Delete
                        </button>

                    </div>
                ))
            )}

        </div>
    )
}

export default App