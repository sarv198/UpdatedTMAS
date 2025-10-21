# TMAS Academy - Frontend

This is the Next.js frontend for The Math and Science Academy (TMAS), an educational non-profit providing free math and science resources.

## Tech Stack

- **Next.js 15** with React 19
- **TypeScript**
- **Tailwind CSS v4** with PostCSS
- **Lucide React** for icons
- **Turbopack** for fast builds

## Getting Started

Run the development server:

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser.

Other commands:

```bash
npm run build   # Build for production with Turbopack
npm start       # Start production server
```

## Project Structure

```
client/
├── components/      # Reusable React components
│   ├── Navigation.tsx
│   └── Footer.tsx
├── pages/          # Next.js pages
│   ├── index.tsx   # Home page
│   ├── about.tsx   # About page
│   ├── resources.tsx
│   ├── contact.tsx
│   ├── join.tsx
│   ├── donate.tsx
│   └── api/        # API routes
├── styles/
│   └── globals.css # Global Tailwind styles
└── public/         # Static assets
```

## Pages

- **Home** (`/`) - Landing page with mission and features
- **About** (`/about`) - Organization information
- **Resources** (`/resources`) - Educational materials
- **Contact** (`/contact`) - Contact form
- **Join** (`/join`) - Community/Discord info
- **Donate** (`/donate`) - Support the mission

## Components

- **Navigation** - Site-wide navigation bar
- **Footer** - Site-wide footer with social links

## Learn More

- [Next.js Documentation](https://nextjs.org/docs)
- [Tailwind CSS v4](https://tailwindcss.com/docs)
- [Lucide Icons](https://lucide.dev)
