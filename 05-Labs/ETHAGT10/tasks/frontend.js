import React, { useState, useEffect } from 'react';

// Componente de lista de usuários com paginação
const UserList = () => {
  const [users, setUsers] = useState([]);
  const [page, setPage] = useState(1);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchUsers();
  }, [page]);

  const fetchUsers = async () => {
    setLoading(true);
    const res = await fetch(`/api/users?page=${page}`);
    const data = await res.json();
    setUsers(data.users);
    setLoading(false);
  };

  return (
    <div>
      {loading ? (
        <span>Carregando...</span>
      ) : (
        <ul>
          {users.map(u => <li key={u.id}>{u.name}</li>)}
        </ul>
      )}
      <button onClick={() => setPage(p => p - 1)}>Anterior</button>
      <button onClick={() => setPage(p => p + 1)}>Próximo</button>
    </div>
  );
};

export default UserList;
