export default function Footer() {
  return (
    <footer className="bg-slate-900 text-white py-8 mt-16">
      <div className="max-w-7xl mx-auto px-4 text-center">
        <p className="text-slate-400">
          © 2025 TMAS Academy. Making education accessible to everyone.
        </p>
        <div className="flex justify-center gap-6 mt-4">
          <a href="https://instagram.com" target="_blank" rel="noopener noreferrer" className="text-slate-400 hover:text-white">
            Instagram
          </a>
          <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer" className="text-slate-400 hover:text-white">
            LinkedIn
          </a>
          <a href="https://discord.com" target="_blank" rel="noopener noreferrer" className="text-slate-400 hover:text-white">
            Discord
          </a>
        </div>
      </div>
    </footer>
  );
}
