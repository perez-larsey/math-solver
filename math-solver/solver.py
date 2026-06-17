from sympy import *
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table

console = Console()
x, y, z = symbols('x y z')


def solve_expression(expr_str):
    try:
        expr = sympify(expr_str)
    except Exception:
        console.print("[red]Invalid expression. Try something like: x**2 + 3*x - 5[/red]")
        return

    console.print(Panel(f"[bold cyan]Expression:[/bold cyan] {expr}", title="📥 Input"))

    simplified = simplify(expr)
    console.print(f"\n[bold green]✔ Simplified:[/bold green]    {simplified}")

    derivative = diff(expr, x)
    console.print(f"[bold yellow]✔ Derivative (dy/dx):[/bold yellow] {derivative}")

    integral = integrate(expr, x)
    console.print(f"[bold magenta]✔ Integral:[/bold magenta]          {integral} + C")

    try:
        roots = solve(expr, x)
        if roots:
            console.print(f"[bold red]✔ Roots (f(x)=0):[/bold red]    {roots}")
        else:
            console.print("[bold red]✔ Roots:[/bold red] No real roots found")
    except Exception:
        console.print("[bold red]✔ Roots:[/bold red] Could not solve")


def solve_limit():
    console.print("\n[bold cyan]--- Limit Solver ---[/bold cyan]")
    console.print("[dim]Enter expression (use x as variable):[/dim]")
    expr_str = input("f(x) = ").strip()
    console.print("[dim]Approaching value (e.g. 0, oo, -oo):[/dim]")
    point_str = input("x → ").strip()

    try:
        expr = sympify(expr_str)
        point = sympify(point_str)
        result = limit(expr, x, point)
        console.print(Panel(
            f"[bold green]lim (x → {point}) of {expr} = {result}[/bold green]",
            title="📐 Limit Result"
        ))
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")


def solve_matrix():
    console.print("\n[bold cyan]--- Matrix Operations ---[/bold cyan]")
    console.print("[dim]Enter matrix size (e.g. 2 for 2x2, 3 for 3x3):[/dim]")

    try:
        n = int(input("Size: ").strip())
        rows = []
        console.print(f"[dim]Enter {n} rows, each with {n} numbers separated by spaces:[/dim]")
        for i in range(n):
            row = list(map(sympify, input(f"Row {i+1}: ").strip().split()))
            rows.append(row)

        M = Matrix(rows)

        # Display matrix as table
        table = Table(title="Input Matrix", show_header=False)
        for _ in range(n):
            table.add_column()
        for row in M.tolist():
            table.add_row(*[str(v) for v in row])
        console.print(table)

        det = M.det()
        console.print(f"\n[bold green]✔ Determinant:[/bold green] {det}")

        try:
            inv = M.inv()
            console.print(f"[bold yellow]✔ Inverse:[/bold yellow]\n{inv}")
        except Exception:
            console.print("[bold yellow]✔ Inverse:[/bold yellow] Matrix is not invertible")

        eigenvals = M.eigenvals()
        console.print(f"[bold magenta]✔ Eigenvalues:[/bold magenta] {eigenvals}")

        eigenvects = M.eigenvects()
        console.print("[bold red]✔ Eigenvectors:[/bold red]")
        for val, mult, vecs in eigenvects:
            for v in vecs:
                console.print(f"   λ={val} → {v.T}")

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")


def solve_system():
    console.print("\n[bold cyan]--- System of Equations Solver ---[/bold cyan]")
    console.print("[dim]How many equations?[/dim]")

    try:
        n = int(input("Number: ").strip())
        equations = []
        syms = [x, y, z][:n]

        console.print(f"[dim]Enter each equation set to 0 (e.g. x + 2*y - 5):[/dim]")
        for i in range(n):
            eq_str = input(f"Eq {i+1}: ").strip()
            equations.append(sympify(eq_str))

        solution = solve(equations, syms)

        if solution:
            console.print(Panel(
                f"[bold green]Solution: {solution}[/bold green]",
                title="✅ System Result"
            ))
        else:
            console.print("[red]No solution found.[/red]")

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")


def main():
    console.print(Panel(
        Text("Math Expression Solver", justify="center", style="bold white"),
        subtitle="Calculus • Limits • Matrices • Systems",
        style="bold blue"
    ))

    menu = """
[bold white]What do you want to solve?[/bold white]

  [cyan]1[/cyan] — Expression  (simplify, derivative, integral, roots)
  [cyan]2[/cyan] — Limit
  [cyan]3[/cyan] — Matrix operations
  [cyan]4[/cyan] — System of equations
  [cyan]q[/cyan] — Quit
"""

    while True:
        console.print(menu)
        choice = input(">>> ").strip().lower()

        if choice == "q":
            console.print("[dim]Goodbye 👋[/dim]")
            break
        elif choice == "1":
            console.print("\n[dim]Enter expression (use x as variable):[/dim]")
            expr_str = input("f(x) = ").strip()
            if expr_str:
                solve_expression(expr_str)
        elif choice == "2":
            solve_limit()
        elif choice == "3":
            solve_matrix()
        elif choice == "4":
            solve_system()
        else:
            console.print("[red]Invalid choice. Enter 1, 2, 3, 4 or q.[/red]")


if __name__ == "__main__":
    main()