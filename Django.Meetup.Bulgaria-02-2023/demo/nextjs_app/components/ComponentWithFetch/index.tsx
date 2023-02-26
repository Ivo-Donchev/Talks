import useSWR from 'swr'
import Card from '@mui/material/Card';
import Box from '@mui/material/Box';
import CircularProgress from '@mui/material/CircularProgress';


export default ({crud}) => {
  const [
    createCount,
    selectCount,
    updateCount,
    deleteCount
  ] = crud;
  const { isLoading } = useSWR(
    `http://localhost:8000/api/${createCount}/${selectCount}/${updateCount}/${deleteCount}/`,
    fetch
  )

  return (
    <Card sx={{ width: '15vw', height: 40, backgroundColor: 'white', textAlign: 'center' }} >

    {
      isLoading
      ? <Box><CircularProgress /></Box>
      :  (
        <>
          <div>C / R / U / D</div>
          <div>{createCount} / {selectCount} / {updateCount} / {deleteCount}</div>
        </>
      )
    }
    </Card>
  )
}
