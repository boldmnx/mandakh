using System;
using System.Collections.Generic;

class MenuItem
{
    public string Name { get; set; }
    public decimal Price { get; set; }

    public MenuItem(string name, decimal price)
    {
        Name = name;
        Price = price;
    }

    public virtual string Display()
    {
        return $"{Name}: ${Price:F2}";
    }
}

class Food : MenuItem
{
    public string Cuisine { get; set; }

    public Food(string name, decimal price, string cuisine) : base(name, price)
    {
        Cuisine = cuisine;
    }

    public override string Display()
    {
        return $"{Name} ({Cuisine}): ${Price:F2}";
    }
}

class Drink : MenuItem
{
    public string Size { get; set; }

    public Drink(string name, decimal price, string size) : base(name, price)
    {
        Size = size;
    }

    public override string Display()
    {
        return $"{Name} ({Size}): ${Price:F2}";
    }
}

class Program
{
    static void PrintMenuItem(MenuItem menuItem)
    {
        Console.WriteLine(menuItem.Display());
    }

    static void Main()
    {
        Food pizza = new Food("Pizza", 12.99m, "Italian");
        Drink coffee = new Drink("Coffee", 2.99m, "Medium");

        Console.WriteLine(pizza.Display());  // Output: Pizza (Italian): $12.99
        Console.WriteLine(coffee.Display()); // Output: Coffee (Medium): $2.99

        // Example usage of polymorphism
        List<MenuItem> items = new List<MenuItem> { pizza, coffee };

        foreach (MenuItem item in items)
        {
            PrintMenuItem(item);
        }
    }
}
